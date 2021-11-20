"""
4. Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский, и дочерний классы
получили новое значение цены. Следует проверить это, вызвав соответствующий метод родительского класса и функцию
дочернего (функция, отвечающая за отображение информации о товаре в одной строке).
"""


class ItemDiscount:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def change_price(self):
        new_price = int(input(f'Введите новую цена для товара {self.name}: '))
        setattr(self, 'price', new_price)


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'Товар: {self.name}, цена: {self.price}'


prod_1 = ItemDiscountReport('Product', 1000)
print(prod_1.get_parent_data())

prod_1.change_price()
print(prod_1.get_parent_data())
