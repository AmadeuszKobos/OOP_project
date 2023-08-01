import csv


def color(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"


class Item:
    company_name = "Chihuahua"
    all_items = []

    def __init__(self, name: str = "", price: float = 0, quantity=0):
        # Run validation for received arguments
        assert price >= 0, f"Price: {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity: {quantity} is not greater than or equal to zero"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.__quantity = quantity

        Item.all_items.append(self)

        print(color("New item created!!!", "33"))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    def calculate_total_price(self):
        print(f"The prize of all {self.__name}s is equal to {self.__price * self.__quantity}")

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', '{self.__price}', '{self.__quantity}')"

    @classmethod
    def initiate_from_csv(cls, item):
        cls(
            name=item.get('name'),
            price=float(item.get('price')),
            quantity=int(item.get('quantity'))
        )


    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


