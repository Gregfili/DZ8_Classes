# main.py
from product import Product
from customer import Customer
from order import Order
from discount import Discount

# Создание продуктов
product1 = Product("Moloko", 100)
product2 = Product("Hleb", 50)
product3 = Product("Maslo", 200)

# Создание клиентов
customer1 = Customer("Tatjana")
customer2 = Customer("Sergej")

# Создание заказов
order1 = Order([product1, product2])
order2 = Order([product3])

# Добавление заказов клиентам
customer1.add_order(order1)
customer2.add_order(order2)

# Применение скидок
discount = Discount("Sezonnaja skidka", 10)
discounted_price = discount.seasonal_discount(product1.price)
print(f"Originalnaja cena: {product1.price}, Cena so skidkoj: {discounted_price}")

promo_discounted_price = discount.promo_code_discount(product2.price, "PROMO20")
print(f"Originalnaja cena: {product2.price}, Cena po promocodu: {promo_discounted_price}")

# Подсчет общего количества заказов и общей суммы заказов для всех клиентов
total_orders = Order.get_total_orders()
total_amount = Order.get_total_amount()

print(f"Obschee kolichestvo zakazov: {total_orders}")
print(f"Obschaja summa: {total_amount}")

# Вывод информации о клиентах, заказах и продуктах
print(customer1)
print(customer2)
print(order1)
print(order2)
print(product1)
print(product2)
print(product3)


