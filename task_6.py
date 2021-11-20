"""
6. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая в первом классе будет отвечать
за вывод названия товара, а вторая — его цены. Далее реализовать выполнение каждой из функции тремя способами.
"""


class ItemDiscount:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def change_price(self):
        new_price = int(input(f'Введите новую цена для товара {self.name}: '))
        setattr(self, 'price', new_price)


class ItemDiscountReport1(ItemDiscount):

    def get_info(self):
        return self.name


class ItemDiscountReport2(ItemDiscount):

    def get_info(self):
        return self.price


prod_1 = ItemDiscountReport1('Product', 1000)
prod_2 = ItemDiscountReport2('Test', 999)

# 1 способ
print(prod_1.get_info())
print(prod_2.get_info())

# 2 способ
print(ItemDiscountReport1.get_info(prod_1))
print(ItemDiscountReport2.get_info(prod_2))

# 3 способ
print(prod_1.__getattribute__('get_info')())
print(prod_2.__getattribute__('get_info')())

# 4 способ
print(ItemDiscountReport1('Product_n', 222).get_info())
print(ItemDiscountReport2('Test_n', 333).get_info())
