import csv

with open("/Users/zhengyanglumacmini/Desktop/Projects/lm_smt/z3_fasttext_preds.csv", 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    data = [(int(row[0]), int(row[1])) for row in reader]

#calculate the accuracy
size = len(data)
correct = 0
for record in data:
    if record[0] == record[1]:
        correct += 1
accuracy = correct / size
print(f"Accuracy: {accuracy:.4f}")

# calculate the precision
true_pos = 0
false_pos = 0
for record in data:
    if record[0] == 1 and record[1] == 1:
        true_pos += 1
    elif record[0] == 1 and record[1] == 0:
        false_pos += 1
precision = true_pos / (true_pos + false_pos)
print(f"Precision: {precision:.4f}")

# calculate the recall
true_pos = 0
false_neg = 0
for record in data:
    if record[0] == 1 and record[1] == 1:
        true_pos += 1
    elif record[0] == 0 and record[1] == 1:
        false_neg += 1
recall = true_pos / (true_pos + false_neg)
print(f"Recall: {recall:.4f}")