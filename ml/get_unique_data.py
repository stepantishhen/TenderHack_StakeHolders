from difflib import SequenceMatcher
import pandas as pd


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


logs = pd.read_csv("all_logs.csv",
                   delimiter=";",
                   header=None,
                   names=['log_id','log_time', 'log'])
print(logs.head())

unique_logs = []

logs_value = logs["log"].values
number_of_logs = len(logs_value)
number_of_processed_logs = 0

for log_value in logs_value:
    print((number_of_processed_logs / number_of_logs) * 100)
    is_unique = True
    for unique_log in unique_logs:
        if similar(log_value[:50], unique_log[:50]) >= 0.7:
            is_unique = False
            break
    if is_unique:
        unique_logs.insert(0, log_value.replace("\n", " ").strip())
    number_of_processed_logs += 1

txt_file = open("unique_logs3.txt", "w")
for log in unique_logs:
    txt_file.write(log + "\n")
