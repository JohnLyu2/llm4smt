import csv
import matplotlib.pyplot as plt

# read the csv file
with open("/Users/zhengyanglumacmini/Desktop/Projects/lm_smt/dataset_prepare/sage2_stats.csv", 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    # read into data and make the second and third column into int
    data = [(row[0], int(row[1]), int(row[2])) for row in reader]

char_len = [row[1] for row in data]
word_len = [row[2] for row in data]

min_char_len = min(char_len)
max_char_len = max(char_len)
mean_char_len = sum(char_len) / len(char_len)
med_char_len = char_len[len(char_len) // 2]
print(f"Character length: min {min_char_len}; max {max_char_len}; mean {mean_char_len}; median {med_char_len}")
# draw the histogram for char_len
# plt.hist(char_len, bins=10)
# plt.xlabel("Character length")
# plt.ylabel("Frequency")
# plt.show()


min_word_len = min(word_len)
max_word_len = max(word_len)
mean_word_len = sum(word_len) / len(word_len)
med_word_len = word_len[len(word_len) // 2]
print(f"Word length: min {min_word_len}; max {max_word_len}; mean {mean_word_len}; median {med_word_len}")
# draw the histogram for word_len
# plt.hist(word_len, bins=10)
# plt.xlabel("Word length")
# plt.ylabel("Frequency")
# plt.show()

