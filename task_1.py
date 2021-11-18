"""
1. Написать функцию, реализующую вывод таблицы умножения размерностью AｘB.
Первый и второй множитель должны задаваться в виде аргументов функции.
Значения каждой строки таблицы должны быть представлены списком, который формируется в цикле.
После этого осуществляется вызов внешней lambda-функции, которая формирует на основе списка строку.
Полученная строка выводится в главной функции.
Элементы строки (элементы таблицы умножения) должны разделяться табуляцией.
"""

list_to_str = lambda mult_table: '\t'.join([str(i) for i in mult_table])


def table_multiplication(columns: int, line: int):
    for i in range(line + 1)[1:]:
        row = []
        for j in range(columns + 1)[1:]:
            if i == 0:
                row.append(j)
            elif j == 0:
                row.append(i)
            else:
                row.append(i * j)
        print(list_to_str(row))


table_multiplication(3, 7)
