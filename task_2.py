"""
2. Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением,
целое оно или дробное. Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать значение True, иначе False.
"""


def comparison_nums(num):
    a, b = num.split('.')
    return a == b


def int_or_float(n):
    try:
        if '.' in n:
            float(n)
            print('Дробное')
            print(comparison_nums(n))
        else:
            int(n)
            print('Целое')
    except ValueError as err:
        print('Попробуйте еще раз')


def main():
    while True:
        raw_input = input('Для выхода введите q\nВведите число: ')
        if raw_input.lower() == 'q':
            break
        else:
            int_or_float(raw_input)


if __name__ == '__main__':
    main()
