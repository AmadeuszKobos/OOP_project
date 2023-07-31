def color(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"


class Item:
    company_name = "Chihuahua"

    def __init__(self, name: str = "", price: float = 0, quantity=0):
        assert price >= 0, f"Price: {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity: {quantity} is not greater than or equal to zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        print(color("New item created!!!", "33"))

    def calculate_total_price(self):
        print(f"The prize of all {self.name}s is equal to {self.price * self.quantity}")


# Creating instances of a class Item
phone = Item()
phone.name = "Phone"
phone.price = 100
phone.quantity = 5

laptop = Item(name="Laptop", price=1000, quantity=10)

# Calling items methods
phone.calculate_total_price()
laptop.calculate_total_price()

print(color(f"This is called from class {Item.company_name}, this is called from instance {phone.company_name}", "34"))
