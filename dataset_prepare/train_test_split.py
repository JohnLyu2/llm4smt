import os
import csv
import random

FILE_PATH = "/Users/zhengyanglumacmini/Desktop/Projects/lm_smt/bin_sage2/raw/merged_3_mini.csv"

def split_raw_data(file_path, test_percentage):
    assert os.path.exists(file_path)
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        rawdata = [row for row in reader]
    # shuffle the rawdata
    random.shuffle(rawdata)
    test_size = int(len(rawdata) * test_percentage)
    train_size = len(rawdata) - test_size
    train_file_path = file_path.replace(".csv", "_train.csv")
    test_file_path = file_path.replace(".csv", "_test.csv")
    with open(train_file_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rawdata[:train_size])
    with open(test_file_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rawdata[train_size:])

split_raw_data(FILE_PATH, 0.3)