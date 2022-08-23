# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def create_folders():
    for i in range(10):
            folder_name = "dir_{}".format(i)
            os.mkdir(folder_name)


def delete_folders():
    for i in range(10):
        folder_name = "dir_{}".format(i)
        os.rmdir(folder_name)

create_folders()
delete_folders()