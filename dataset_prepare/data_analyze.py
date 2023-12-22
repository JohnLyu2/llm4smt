import csv
from smt_preprocess import *

# data header: instance, solver, result, time
# z3_csv_data = "/Users/zhengyanglumacmini/Desktop/Projects/lm_smt/bin_sage2/raw/z3_3_mini.csv"
# cvc5_csv_data = "/Users/zhengyanglumacmini/Desktop/Projects/lm_smt/bin_sage2/raw/cvc5_3_mini.csv"

# with open(z3_csv_data, 'r') as f:
#     reader = csv.reader(f)
#     header = next(reader)
#     z3_data = [[row[0], (row[2] == 'sat' or row[2] == 'unsat')] for row in reader]

# with open(cvc5_csv_data, 'r') as f:
#     reader = csv.reader(f)
#     header = next(reader)
#     cvc5_data = [[row[0], (row[2] == 'sat' or row[2] == 'unsat')] for row in reader]

# # create a new merged z3 and cvc5 data by matching the instance
# merged_data = []
# for z3_record in z3_data:
#     for cvc5_record in cvc5_data:
#         if z3_record[0] == cvc5_record[0]:
#             merged_data.append([z3_record[0], z3_record[1], cvc5_record[1]])

# with open("/Users/zhengyanglumacmini/Desktop/Projects/lm_smt/bin_sage2/raw/merged_3_mini.csv", 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(["instance", "z3", "cvc5"])
#     writer.writerows(merged_data)

# size = len(data)

# solved = 0
# for record in data:
#     if record[2] == 'sat' or record[2] == 'unsat':
#         solved += 1

# print("Solved: ", solved)
# print("Total: ", size)

# def cc_to_mini_path(cc_path):
#     cc_prefix = "/home/z52lu/fastsmtData/smt_data/sage2/all/"
#     mini_prefix = "/Users/zhengyanglumacmini/Desktop/smt-lib/QF_BV/Sage2/"
#     mini_path = cc_path.replace(cc_prefix, mini_prefix)
#     return mini_path

# def mini_to_cc_path(mini_path):
#     mini_prefix = "/Users/zhengyanglumacmini/Desktop/smt-lib/QF_BV/Sage2/"
#     cc_prefix = "/home/z52lu/fastsmtData/smt_data/sage2/all/"
#     cc_path = mini_path.replace(mini_prefix, cc_prefix)
#     return cc_path

# with open("/Users/zhengyanglumacmini/Desktop/Projects/lm_smt/bin_sage2/raw/merged_3_mini_train.csv", 'r') as f:
#     reader = csv.reader(f)
#     header = next(reader)
#     merged_data = [row for row in reader]

# with open("/Users/zhengyanglumacmini/Desktop/Projects/lm_smt/bin_sage2/raw/merged_3_cc_train.csv", 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(["instance", "z3", "cvc5"])
#     for record in merged_data:
#         cc_path = mini_to_cc_path(record[0])
#         writer.writerow([cc_path, record[1], record[2]])
    
# cleaned_merged_data = []
# for record in merged_data:
#     path = record[0]
#     if not is_empty_file(path):
#         cleaned_merged_data.append(record)

# with open("/Users/zhengyanglumacmini/Desktop/Projects/lm_smt/bin_sage2/raw/merged_3_mini.csv", 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(["instance", "z3", "cvc5"])
#     writer.writerows(cleaned_merged_data)

# record total instance number and how many are solved and not
with open("/Users/zhengyanglumacmini/Desktop/Projects/lm_smt/bin_sage2/raw/merged_3_mini.csv", 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    data = [row for row in reader]

size = len(data)
z3_solved = 0
for record in data:
    if record[1] == 'True':
        z3_solved += 1
print(f"Total: {size}, Z3 Solved: {z3_solved}, Z3 Not solved: {size - z3_solved}")
        