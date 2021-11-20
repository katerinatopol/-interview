"""
2. Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться, что при сохранении текущей
логики работы программы будет сгенерирована ошибка выполнения.
"""


class ItemDiscount:

    def __init__(self, name, price):

        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'Товар: {self.__name}, цена: {self.__price}'


prod_1 = ItemDiscountReport('Product', 1000)
print(prod_1.get_parent_data())

# AttributeError: 'ItemDiscountReport' object has no attribute '_ItemDiscountReport__name'
