class Product:
    def __init__(self, name, price, quantity=1, defective=False):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.defective = defective

    # @property
    # def price(self):
    #     return self.price
    #
    # @price.setter
    # def price(self, number):
    #     self.price += number

    def get_price(self):
        return self.price

    def set_price(self, amount):
        self.price = amount
        return self.price

    def get_quantity(self):
        if self.quantity == 0:
            raise Exception('Product is not available')
        else:
            return self.quantity

    def set_quantity(self, amount):
        self.quantity += amount
        return self.price

    def __str__(self):
        return f'{self.name}, {self.price}, {self.quantity}'


class HouseholdChemicals(Product):

    type_of_goods = 'household chemicals'

    def __str__(self):
        return f'Type of goods is {self.type_of_goods} name {self.name} price {self.price} quantity {self.quantity}'


class Food(Product):
    pass


class PerishableProducts(Product):
    pass


class ExciseProducts(Product):
    pass


class FlammableProducts(Product):
    pass


class BreakableProducts(Product):
    pass


a = BreakableProducts('Vaza', '22', '2')

print(a.get_quantity())

a.set_quantity(-2)
print(a.get_quantity())