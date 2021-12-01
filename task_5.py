"""
5. Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть строковых значений
заменить на значения типа example345 (строка+число). Далее — усовершенствовать вторую функцию из предыдущего примера
(функцию извлечения данных). Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям:
вывод первого вхождения, вывод всех вхождений. Реализовать замену всех найденных подстрок на новое значение и вывод
всех подстрок, состоящих из букв и цифр, например: example345.
"""

import os
import re
from random import randint, choice
from string import ascii_letters


def create_file(file_name):
    if os.path.exists(file_name):
        print('Файл существует')
    else:
        n_lst = list(range(randint(5, 20)))
        s_lst = [''.join(choice(ascii_letters) for i in range(randint(2, 7))) for _ in range(randint(5, 20))]
        for ind, el in enumerate(s_lst):  # добавлено
            if ind % 2 == 0:
                s_lst[ind] = f"{el}{randint(1, 500)}"
        res_lst = zip(n_lst, s_lst)

        with open(file_name, 'a') as f:
            for el in res_lst:
                f.writelines(f'{el[0]} - {el[1]}\n')

        file_read(file_name, substr='a', new_val=None, mode=1)


def file_read(file, substr=None, new_val=None, mode=0):
    with open(file, encoding='utf') as f:
        if mode == 0:  # просто печать
            text = f.readlines()
            for line in text:
                print(line)
        elif mode == 1 and substr:  # вывод первого вхождения
            text = f.read()
            pattern = f'{substr}'
            print(pattern)
            print(re.search(pattern, text))
        elif mode == 2 and substr:  # вывод всех вхождений
            text = f.read()
            print(re.findall(substr, text))
        elif mode == 3 and substr and new_val:  # замена всех найденных подстрок на новое значение
            text = f.read()
            text = re.sub(substr, new_val, text)


if __name__ == '__main__':
    create_file('test_file.txt')
