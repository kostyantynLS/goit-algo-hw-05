'''
Розробіть Python-скрипт для аналізу файлів логів. Скрипт повинен вміти читати лог-файл, 
переданий як аргумент командного рядка, і виводити статистику за рівнями логування 
наприклад, INFO, ERROR, DEBUG. Також користувач може вказати рівень логування як другий 
аргумент командного рядка, щоб отримати всі записи цього рівня.

Для виконання завдання візьміть наступний приклад лог-файлу:

2024-01-22 08:30:01 INFO User logged in successfully.
2024-01-22 08:45:23 DEBUG Attempting to connect to the database.
2024-01-22 09:00:45 ERROR Database connection failed.
2024-01-22 09:15:10 INFO Data export completed.
2024-01-22 10:30:55 WARNING Disk usage above 80%.
2024-01-22 11:05:00 DEBUG Starting data backup process.
2024-01-22 11:30:15 ERROR Backup process failed.
2024-01-22 12:00:00 INFO User logged out.
2024-01-22 12:45:05 DEBUG Checking system health.
2024-01-22 13:30:30 INFO Scheduled maintenance.
'''

from colorama import Fore, Back, Style
#from collections import namedtuple
import re, sys

def parse_log_file(line: str) -> dict:
    log_dic = dict()
    l_data, l_time, l_level, l_msg = line.split(" ", maxsplit = 3) #список міститиме щонайбільше елементів maxsplit+1
    log_dic["date"] = l_data
    log_dic["time"] = l_time
    log_dic["level"] = l_level
    log_dic["msg"] = l_msg
    return log_dic

def load_logs(file_path: str) -> list:
    with open(file_path, "r", encoding="utf-8") as log_file:
        log_info = list()
        while True:
            line = log_file.readline()
            line = re.sub("\n", "", line)
            if len(line)>0:
                log_info.append(parse_log_file(line))
            else:
                break
    return log_info

def count_logs_by_level(logs: list) -> dict:
    events = dict()
    for event_in_logs in logs:
        event_name = event_in_logs["level"]
        if event_name in events:
            events[event_name] = events[event_name]+1
        else:
            events[event_name] = 1
    return events

def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_events = list()
    for event_in_logs in logs:
        if event_in_logs["level"] == level:
            filtered_events.append(event_in_logs)
    return filtered_events

def display_log_counts(counts: dict):
    print('Рівень логування | Кількість\n'
          '-----------------|----------')
    for event_name, event_count in counts.items():
        event_string = event_name + " "*(17-len(event_name)) + "| " + str(event_count)
        print(event_string)

def filter_logs_by_level(log_list: list, log_level: str):
    if log_level>"":
        filtered_list = filter_logs_by_level(log_list, log_level)
        if len(filtered_list)>0:
            print(f"\nДеталі логів для рівня '{log_level}':")
            for msgs in filtered_list:
                text = msgs["date"] + " " + msgs["time"] + " " + msgs["level"] + " " + msgs["msg"]
                print(text)
        else:
            print(f"\nДеталі логів для рівня '{log_level}' не виявлені")

def main():
    # checking arguments to file

    if len(sys.argv) > 1:
        log_file = sys.argv[1]
        if len(sys.argv) == 3:
            log_level = sys.argv[2]
            log_level = log_level.upper()
        else:
            log_level = ""
    else:
        print('Error: error in arguments!')
        print('run: <log_file> [log_level]')
        exit()

    log_list = load_logs(log_file)
    event_dic = count_logs_by_level(log_list)
    display_log_counts(event_dic)
    filter_logs_by_level(log_list, log_level)

if __name__ == "__main__":
    main()
