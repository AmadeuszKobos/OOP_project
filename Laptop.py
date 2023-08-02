from Item import Item


class Laptop(Item):
    def __init__(self, name: str, price: float, quantity=0, battery_capacity=2400):
        super().__init__(name, price, quantity)

        self.__battery_capacity = battery_capacity

    @property
    def battery_capacity(self):
        return self.__battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, item):
        self.__battery_capacity = item

    @classmethod
    def initiate_from_csv(cls, item):
        cls(
            name=item.get('name'),
            price=float(item.get('price')),
            quantity=int(item.get('quantity')),
            battery_capacity=int(item.get('battery_capacity'))
        )