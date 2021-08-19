from datetime import date


class Product:
    def __init__(self, product_type, product_name, price, expiration, quantity=1, defective=False,
                 defective_amount=0):
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
        return sum(self.arrived)

    def sell_goods(self, count):
        self.product._quantity -= int(count)
        self.sold.append(count)
        return self.product.quantity

    def get_written_off_goods(self):
        return self.product.defective_amount

    def __str__(self):
        return f'Were arrived {sum(self.arrived)} items of {self.product.product_type}. ' \
               f'{self.product.defective_amount} were written off. Were sold {sum(self.sold)}. Current quantity is ' \
               f'{self.product._quantity}'


class Food(Product):
    def __init__(self, product_type, product_name, price, expiration, quantity=1, defective=False,
                 defective_amount=0, highest_sort=False):
        super().__init__(product_type, product_name, price, expiration, quantity, defective, defective_amount)
        self.highest_sort = highest_sort

    @property
    def sort(self):
        return self.highest_sort

    @sort.setter
    def sort(self, boolean):
        self.highest_sort = boolean


class HouseholdChemicals(Product):
    def __init__(self, product_type, product_name, price, expiration, quantity=1, defective=False,
                 defective_amount=0, harming_goods=False):
        super().__init__(product_type, product_name, price, expiration, quantity, defective, defective_amount)
        self.harming_goods = harming_goods


class PerishableProducts(Product):

    def set_sale(self):
        self.price *= 90
        return self.price


class ExciseProducts(Product):
    def __init__(self, product_type, product_name, price, expiration, amount_consignments_of_good, quantity=1,
                 defective=False, defective_amount=0):
        super().__init__(product_type, product_name, price, expiration, quantity, defective, defective_amount)
        self.amount_consignments_of_good = amount_consignments_of_good
        self.quantity *= (amount_consignments_of_good*10-1)


class FlammableProducts(Product):
    def __init__(self, product_type, product_name, price, expiration, quantity=1, defective=False,
                 defective_amount=0, message='The goods are flammable. Be careful'):
        super().__init__(product_type, product_name, price, expiration, quantity, defective, defective_amount)
        self.message = print(message)


class BreakableProducts(Product):
    def __init__(self, product_type, product_name, price, expiration, quantity=1, defective=False,
                 defective_amount=0, damaged=0):
        super().__init__(product_type, product_name, price, expiration, quantity, defective, defective_amount)
        self.damaged = damaged
        self._quantity -= damaged


bread = Product('bread', 'baton', '55', date(2021, 8, 25), quantity=5, defective=True)
shampoo = Product('shampoo', 'clear hair', '99.99', date(2021, 12, 25), quantity=10)
meat = Product('meat', 'chicken thighs', '124', date(2021, 12, 29))
alcohol = Product('vine', 'red semi sweet', '255', date(2022, 1, 1))
lighter = Product('lighter', 'clipper', '20', date(2023, 1, 1))
plate = Product('plate', 'white plate', '59', date(2023, 1, 1))

bread_management = ProductManagement(bread)
shampoo_management = ProductManagement(shampoo)

# print(shampoo_management.get_goods_arrived())

shampoo_management.sell_goods(5)
shampoo.defective_amount = 1

# print(shampoo_management)

# product_type, product_name, price, expiration, quantity=1, defective=False, defective_amount=0)

cheese = Food('cheese', 'bri', '47.95', date(2021, 8, 29))

# print(cheese.highest_sort)
# cheese.highest_sort = True
# print(cheese.highest_sort)

# gas_bottle = FlammableProducts('gas_bottle', 'AAA-79', '249.99', date(2025, 1, 1), quantity=3)

vine = ExciseProducts('vine', 'Moet', '1790', date(2022, 1, 1), 2)

# print(vine.quantity)

vase = BreakableProducts('vase', 'deep vase', '179.9', date(2030, 1, 1), quantity=5, damaged=4)

# print(vase.quantity)

eggs = PerishableProducts('egg', 'chicken eggs', '2.15', date(2021, 8, 22))

# eggs.set_sale()
# print(eggs.price)
