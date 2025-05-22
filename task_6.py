class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")

    def can_afford(self, customer_money):
        return customer_money >= self.price


class Book(Product):
    def __init__(self, name, author, price, publisher):
        super().__init__(name, price)
        self.author = author
        self.publisher = publisher

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")
        print(f"Publisher: {self.publisher}")
        print("-" * 20)


class Toy(Product):
    def __init__(self, name, price, manufacturer, material):
        super().__init__(name, price)
        self.manufacturer = manufacturer
        self.material = material

    def display_info(self):
        super().display_info()
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Material: {self.material}")
        print("-" * 20)


class Food(Product):
    def __init__(self, name, price, production_date, expiry_date):
        super().__init__(name, price)
        self.production_date = production_date
        self.expiry_date = expiry_date

    def display_info(self):
        super().display_info()
        print(f"Production Date: {self.production_date}")
        print(f"Expiry Date: {self.expiry_date}")
        print("-" * 20)


class Phone(Product):
    def __init__(self, name, price):
        super().__init__(name, price)

    def display_info(self):
        super().display_info()
        print("-" * 20)


products = [
    Book("Java полное руководство 8-е издание", "Герберт Шилдт", 29.99, "Издательсеий дом 'Вильямс'"),
    Toy("BB-8", 49.99, "Джей Той", "Пластик"),
    Food("Молоко", 3.99, "2025-20-05", "2025-30-05"),
    Phone("iPhone 16", 999.99),
    Book("Чистый код", "Роберт Мартин", 39.99, "Prentice Hall"),
    Toy("R2D2", 19.99, "Конструкторская Лавка", "Пластик"),
    Food("Шоколадный батончик", 2.49, "2025-10-05", "2026-06-01"),
    Phone("Iphone 15", 799.99),
]

print("=== ALL PRODUCTS ===")
for product in products:
    product.display_info()

while True:
    try:
        customer_budget = float(input("\nВведите сумму ($): "))
        if customer_budget < 0:
            print("Вы ввели отрицательное число. Введите положительное число.")
            continue
        break
    except ValueError:
        print("Введите число!")

affordable_products = [product for product in products if product.can_afford(customer_budget)]

if affordable_products:
    print(f"\nПродукты, которые вы можете купить (${customer_budget})")
    for product in affordable_products:
        product.display_info()
else:
    print("\nНет доступных продуктов.")