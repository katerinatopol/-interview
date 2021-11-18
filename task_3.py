"""
3. Разработать генератор случайных чисел.
В функцию передавать начальное и конечное число генерации (нуль необходимо исключить).
Заполнить этими данными список и словарь.
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
Вывести содержимое созданных списка и словаря.
"""

# часто повторяются числа.

from datetime import datetime
from time import sleep


def generator_random_number(start, finish):

    if start == 0 or finish == 0 or start >= finish:
        raise ValueError
    else:
        result_str = '1'
        help_num = datetime.now().second // 5
        for _ in range(help_num):
            if help_num == 0:
                help_num = datetime.now().second // 2
            else:
                if datetime.now().second % 2 == 0:
                    result_str += '0'
                    sleep(0.5)
                else:
                    result_str += '1'
                    sleep(0.7)
        result = int(result_str[::-1], 2)

        while result > finish:
            result -= start
        while result < start:
            result += start

        return result


result_lst = []
result_dict = {}

for i in range(10):
    num = (generator_random_number(14, 137))
    result_lst.append(num)
    result_dict[f'elem_{i+1}'] = num

print(result_lst)
print(result_dict)
