from datetime import date


class Product:
    def __init__(self, type_of_good, product_type, product_name, price, expiration, quantity=1, defective=False,
                 defective_amount=0):
        self.type_of_good = type_of_good
        self.product_type = product_type
        self.product_name = product_name
        self._price = float(price)
        self._quantity = int(quantity)
        self._defective = defective
        self.expiration = expiration
        self._defective_amount = defective_amount

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, number):
        self._price = float(number)

    @property
    def quantity(self):
        if self._quantity == 0:
            raise NotAvailable
        else:
            return self._quantity

    @quantity.setter
    def quantity(self, amount):
        self._quantity += int(amount)

    @property
    def is_expired(self):
        if self.expiration >= date.today():
            print('The product is in order.')
        else:
            raise Expired

    @property
    def defective(self):
        if not self._defective:
            print('Product quality is okay.')
        else:
            raise Defective

    @property
    def defective_amount(self):
        return self._defective_amount

    @defective_amount.setter
    def defective_amount(self, amount):
        self._defective_amount += int(amount)
        self._quantity -= int(amount)

    def __str__(self):
        return f'{self.product_name}, {self.price}, {self.quantity}, {self.defective}'


class NotAvailable(Exception):
    def __init__(self, message='The good is not available now.'):
        super().__init__(message)


class Expired(Exception):
    def __init__(self, message='The good was expired.'):
        super().__init__(message)


class Defective(Exception):
    def __init__(self, message='The good is defective.'):
        super().__init__(message)


class ProductManagement:
    def __init__(self, product):
        self.product = product
        self.sold = []
        self.arrived = []

    def get_goods_arrived(self):
        self.arrived.append(self.product.quantity)
        print(f'{self.product.product_type} in amount {self.product.quantity} items were arrived')
        return sum(self.arrived)

    def sell_goods(self, count):
        self.product._quantity -= int(count)
        self.sold.append(count)
        print(f'Were sold {count} items of {self.product.product_type}. Available amount is {self.product._quantity}')
        return self.product.quantity

    def get_written_off_goods(self):
        print(f'{self.product.defective_amount} items of {self.product.product_type} were written off')
        return self.product.defective_amount

    def __str__(self):
        return f'Were arrived {sum(self.arrived)} items of {self.product.product_type}. ' \
               f'{self.product.defective_amount} were written off. Were sold {sum(self.sold)}. Current quantity is ' \
               f'{self.product._quantity}'


bread = Product('Food', 'bread', 'baton', '55', date(2021, 8, 25), quantity=5, defective=True)
shampoo = Product('Household chemicals', 'shampoo', 'clear hair', '99.99', date(2021, 12, 25), quantity=10)
meat = Product('Perishable products', 'meat', 'chicken thighs', '124', date(2021, 12, 29))
alcohol = Product('Excise products', 'vine', 'red semi sweet', '255', date(2022, 1, 1))
lighter = Product('Flammable products', 'lighter', 'clipper', '20', date(2023, 1, 1))
plate = Product('Breakable products', 'plate', 'white plate', '59', date(2023, 1, 1))

bread_management = ProductManagement(bread)
shampoo_management = ProductManagement(shampoo)

print(shampoo_management.get_goods_arrived())

shampoo_management.sell_goods(5)
shampoo_management.sell_goods(2)
shampoo.defective_amount = 1

print(shampoo_management)


