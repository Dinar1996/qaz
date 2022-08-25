# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.

import os


def show_folders():
    folders_and_files = os.listdir(r'C:\Users\Динар\PycharmProjects\pythonProject')

    for i in folders_and_files:
        if os.path.isdir(i):
            print(i)


show_folders()
