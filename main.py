import csv

unic_log = set()

with open('Logs.csv', newline='') as logs:
    reader = csv.DictReader(logs)
    for row in reader:
        unic_log.add(row['log'])

file = open('uniq_logs.txt', 'w')
for log in unic_log:
    print(log, file=file)
file.close()
