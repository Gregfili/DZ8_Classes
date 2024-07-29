
from product import Product

class Order:
    total_orders = 0
    total_amount = 0

    def __init__(self, products):
        self.products = products
        Order.total_orders += 1
        Order.total_amount += self.total_order_amount()

    def total_order_amount(self):
        return sum(product.price for product in self.products)

    def __str__(self):
        return f"Order(products={[str(product) for product in self.products]})"

    @classmethod
    def get_total_orders(cls):
        return cls.total_orders

    @classmethod
    def get_total_amount(cls):
        return cls.total_amount
