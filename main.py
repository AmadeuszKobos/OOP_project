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
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all_items.append(self)

        print(color("New item created!!!", "33"))

    def calculate_total_price(self):
        print(f"The prize of all {self.name}s is equal to {self.price * self.quantity}")

    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"

    @classmethod
    def initiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
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


for instance in Item.all_items:
    print(f'{color("Name: ", "34")} {instance.name}, {color("Price: ", "34")} {instance.price}, {color("Quantity: ", "34")} {instance.quantity}')


Item.initiate_from_csv()
print(Item.all_items)

print(color(Item.is_integer(5.0), "34"))