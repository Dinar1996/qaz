# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil

def copy_this_file():
    file_path, file_name = str(__file__).rsplit('\\', 1)
    print(file_path)
    print(file_name)
    new_file_name = "copy_" + file_name
    new_file_path = file_path + '\\' + new_file_name

    shutil.copyfile(__file__, new_file_path)

copy_this_file()