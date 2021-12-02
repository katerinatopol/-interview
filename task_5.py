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


def create_file(file_name, substr=None, new_val=None, mode=0):
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

        file_read(file_name, substr=substr, new_val=new_val, mode=mode)


def file_read(file, substr=None, new_val=None, mode=0):
    with open(file, encoding='utf') as f:
        if mode == 0:  # просто печать
            lines = f.readlines()
            for line in lines:
                print(line)
        elif substr:  # вывод первого вхождения
            text = f.read()
            match = re.search(substr, text)
            if match is None:
                print(f'Нет вхождений подстроки "{substr}"')
            elif match and mode == 1:
                print(f'Первое вхождение подстроки "{substr}": {match.start()}')
            elif match and mode == 2:  # вывод всех вхождений
                print(f'Все вхождения подстроки "{substr}": {[m.start() for m in re.finditer(substr, text)]}')
            elif match and mode == 3 and new_val:  # замена всех найденных подстрок на новое значение
                f.seek(0)
                lines = f.readlines()
                for line in lines:
                    line = re.sub(substr, new_val, line)
                    print(line)


if __name__ == '__main__':
    create_file('test_file.txt', substr='a', new_val='nnnnn', mode=3)
