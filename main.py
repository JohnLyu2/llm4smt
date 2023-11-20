from transformers import AutoTokenizer
from smt_preprocess import get_assertions

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

assert_text = get_assertions("/Users/zhengyanglumacmini/Desktop/Projects/MachSMT/benchmarks/smt-lib/non-incremental/BV/2017-Preiner-keymaera/accelerating-node2100.smt2")[0]

tokens = tokenizer.tokenize(assert_text)

print(tokens)