from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
import torch
import csv
import numpy as np

if torch.cuda.is_available():
    print("Using GPU")
    device = torch.device("cuda")
else:
    print("Using CPU")
    device = torch.device("cpu")

datafiles = {"train": "/Users/zhengyanglumacmini/Desktop/Projects/lm_smt/bin_sage2/merge_hf_train.csv", "test": "/Users/zhengyanglumacmini/Desktop/Projects/lm_smt/bin_sage2/merge_hf_test.csv"}
solver_data = load_dataset("csv", data_files=datafiles)

def trim_text(examples, max_char_length = 10000):
    trimmed_text = examples["assertions"][:max_char_length]
    return {"assertions": trimmed_text}

trimmed_solver_data = solver_data.map(trim_text)

checkpoint = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(checkpoint, use_fast=True)

def tokenize_function(example):
    return tokenizer(example["assertions"], truncation=True, padding="max_length")

tokenized_solver_data = trimmed_solver_data.map(tokenize_function, batched=True)

z3_solver_data = tokenized_solver_data.map(lambda examples: {'labels': int(examples['z3'])})

z3_model = AutoModelForSequenceClassification.from_pretrained(checkpoint, num_labels=2)

training_args = TrainingArguments(
    output_dir='./model_res',
    num_train_epochs=3,
    per_device_train_batch_size=64,
    per_device_eval_batch_size=64,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10
)

trainer = Trainer(
    model=z3_model,
    args=training_args,
    train_dataset=z3_solver_data["train"],
    eval_dataset=z3_solver_data["test"]
)

trainer.train()
trainer.evaluate()
z3_model.save_pretrained('./distilbert_z3_solver_model')

preds = trainer.predict(z3_solver_data["test"])
pred_labels = np.argmax(preds.predictions, axis=1)

# write the predictions and true lable to a csv, true label is from the test dataset
with open("/Users/zhengyanglumacmini/Desktop/Projects/lm_smt/bin_sage2/z3_solver_preds.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["preds", "labels"])
    for pred, label in zip(pred_labels, z3_solver_data["test"]["labels"]):
        writer.writerow([pred, label])