# discount.py

class Discount:
    def __init__(self, description, discount_percent):
        self.description = description
        self.discount_percent = discount_percent

    @staticmethod
    def apply_discount(price, discount_percent):
        return price * (1 - discount_percent / 100)

    @staticmethod
    def seasonal_discount(price):
        return Discount.apply_discount(price, 10)

    @staticmethod
    def promo_code_discount(price, promo_code):
        promo_discounts = {
            "PROMO10": 10,
            "PROMO20": 20,
        }
        discount_percent = promo_discounts.get(promo_code, 0)
        return Discount.apply_discount(price, discount_percent)

    def __str__(self):
        return f"Discount(description={self.description}, discount_percent={self.discount_percent})"
