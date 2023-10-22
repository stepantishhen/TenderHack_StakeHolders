import csv
import datetime
from dashboard.models import SystemLog


def import_logs(log_file_path):
    with open(log_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for line in reader:
            # Разбор строки лога и создание записи
            log = SystemLog()
            log.category = line["id"]
            log.date_time = line["create_date"]
            log.log = line["log"]
            log.save()


# Вызовите функцию с путем к вашему файлу с логами
import_logs('Logs.csv')
