"""
1. Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться имя файла с расширением.
В функции необходимо реализовать поиск полного пути по имени файла, а затем «выделение» из этого пути имени файла
(без расширения).
"""
import os

FULL_NAME = 'test_file.txt'


def get_path(file_name):
    return os.path.abspath(file_name)


def get_name(path):
    full = os.path.basename(path)
    return os.path.splitext(full)[0]


def main():
    path = get_path(FULL_NAME)
    name = get_name(path)
    print(name)


if __name__ == '__main__':
    main()
