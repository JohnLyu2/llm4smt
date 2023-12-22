import csv
import os

from smt_preprocess import *

CSV_RAW = "/Users/zhengyanglumacmini/Desktop/Projects/lm_smt/bin_sage2/raw/merged_3_mini_train.csv"
FILE2WRITE = "/Users/zhengyanglumacmini/Desktop/Projects/lm_smt/bin_sage2/z3_fasttext_train.txt"
# here token only mean delimited by space
MAX_TOKENS = 1e18

# def cc_to_mini_path(cc_path):
#     cc_prefix = "/home/z52lu/fastsmtData/smt_data/sage2/all/"
#     mini_prefix = "/Users/zhengyanglumacmini/Desktop/smt-lib/QF_BV/Sage2/"
#     mini_path = cc_path.replace(cc_prefix, mini_prefix)
#     return mini_path

with open(CSV_RAW, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    rawdata = [row for row in reader]

with open(FILE2WRITE, 'w') as f:
    # header: instance, solver, result, time
    for record in rawdata:
        path = record[0]
        # print(mini_path)
        # check if the file exists
        if not os.path.exists(path):
            print("File does not exist: ", path)
            continue
        assertions = get_assertions(path)
        label = "no"
        if record[1] == 'True':
            label = "yes"
        label_str = f"__label__{label}"
        print(label_str)
        line = f"{label_str} {assertions}\n"
        if len(assertions.split()) < MAX_TOKENS:
            f.write(line)
  

# print(assertions)

