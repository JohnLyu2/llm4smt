import os
import csv

from smt_preprocess import *

bench_dir = "/Users/zhengyanglumacmini/Desktop/smt-lib/QF_BV/Sage2/"
output_file = "/Users/zhengyanglumacmini/Desktop/Projects/lm_smt/dataset_prepare/sage2_stats.csv"

path_lst = []
for root, dirs, files in os.walk(bench_dir):
    for file in files:
        if file.endswith(".smt2"):
            path_lst.append(os.path.join(root, file))

count_dist = {}
for path in path_lst:
    file_name = os.path.basename(path)
    ass_txt = get_assertions(path)
    char_len = len(ass_txt)
    if char_len:
        split_text = ass_txt.split()
        word_len = len(split_text)
        print(f"assertations char len {char_len}; word len {word_len}")
        count_dist[file_name] = (char_len, word_len)

# write count_dist to a csv
with open(output_file, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["file_name", "char_len", "word_len"])
    for key, value in count_dist.items():
        writer.writerow([key, value[0], value[1]])
        
