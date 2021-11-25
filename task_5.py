"""
5. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса (метод init, в который должна передаваться
переменная — скидка), и перегрузку метода str дочернего класса. В этом методе должна пересчитываться цена и
возвращаться результат — цена товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать
дочерний и родительский классы (вторая и третья строка после объявления дочернего класса).
"""


class ItemDiscount:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def change_price(self):
        new_price = int(input(f'Введите новую цена для товара {self.name}: '))
        setattr(self, 'price', new_price)


class ItemDiscountReport(ItemDiscount):

    def __init__(self, name, price, discount=0):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        return f'Товар: {self.name}, цена: {self.price - self.price * self.discount / 100}'


prod_1 = ItemDiscountReport('Product', 1000, 21)
print(prod_1)
