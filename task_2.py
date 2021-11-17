"""
2. Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath):

Функция принимает имя каталога и распечатывает его содержимое
в виде «путь и имя файла», а также любые другие
файлы во вложенных каталогах.

Эта функция подобна os.walk. Использовать функцию os.walk
нельзя. Данная задача показывает ваше умение работать с
вложенными структурами.
"""
import os


def print_directory_contents(sPath: str):
    for el in os.listdir(sPath):
        path_el = fr'{sPath}\{el}'
        if os.path.isdir(path_el):
            print_directory_contents(path_el)
        else:
            name_el = os.path.basename(path_el)
            print(f'Путь: {path_el}, имя: {name_el}')


print_directory_contents(r'C:\Users\Katerina\test')
