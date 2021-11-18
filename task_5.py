"""
5. Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться фиксированная
ежемесячная сумма пополнения вклада. Необходимо в главной функции реализовать вложенную функцию подсчета процентов
для пополняемой суммы. Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего.
Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев.
Вложенная функция возвращает сумму дополнительно внесенных средств (с процентами), а главная функция — общую сумму
по вкладу на конец периода.
"""

PRODUCTS = (
    {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5},
    {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5},
    {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5},
)


def check_valid_data(amount, term):
    product = None
    for i in PRODUCTS:
        if i['begin_sum'] <= amount < i['end_sum'] and term in i.keys():
            product = i
    if product:
        return True, product
    else:
        return False, None


def calc_deposit(amount, term, add, product):
    percent = product[term]
    for month in range(term):
        profit = amount * percent / 100 / 12
        amount += profit

    def add_sum(term, add, percent):
        for month in range(term - 2):
            profit = add * percent / 100 / 12
            add += profit
        return add

    return round(amount + add_sum(term, add, percent), 2)


if __name__ == '__main__':

    while True:
        amount = int(input('Введите сумму вклада: '))
        term = int(input('Введите срок вклада: '))
        add = int(input('Введите сумму ежемесячного платежа: '))
        check, product = check_valid_data(amount, term)
        if not check:
            print('Введены не корректные данные, попробуйте еще раз')
        else:
            break

    sum_amount = calc_deposit(amount, term, add, product)
    print(f'Сумма вклада на конец срока: {sum_amount}')
