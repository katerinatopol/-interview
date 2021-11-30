"""
4. Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение. Необходимо открыть файл и подготовить
два списка: с текстовой и числовой информацией. Для создания списков использовать генераторы. Применить к спискам
функцию zip(). Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение. Вызвать вторую функцию. В нее должна передаваться
ссылка на созданный файл. Во второй функции необходимо реализовать открытие файла и простой построчный вывод
содержимого. Вся программа должна запускаться по вызову первой функции.
"""
import os
from random import randint, choice
from string import ascii_letters


def create_file(file_name):
    if os.path.exists(file_name):
        print('Файл существует')
    else:
        n_lst = list(range(randint(5, 20)))
        s_lst = [''.join(choice(ascii_letters) for i in range(randint(2, 7))) for _ in range(randint(5, 20))]
        res_lst = zip(n_lst, s_lst)

        with open(file_name, 'a') as f:
            for el in res_lst:
                f.writelines(f'{el[0]} - {el[1]}\n')

        file_read(file_name)


def file_read(file):
    with open(file, encoding='utf') as f:
        lines = f.readlines()
        for line in lines:
            print(line)


if __name__ == '__main__':
    create_file('test_file.txt')
