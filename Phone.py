from Item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones: int = 0):
        super().__init__(name, price, quantity)

        assert broken_phones >= 0, f"Broken phones number {broken_phones} is not correct number"

        self.__broken_phones = broken_phones

    @property
    def broken_phones(self):
        return self.__broken_phones

    @broken_phones.setter
    def broken_phones(self, value):
        self.__broken_phones = value

    @classmethod
    def initiate_from_csv(cls, item):
        cls(
            name=item.get('name'),
            price=float(item.get('price')),
            quantity=int(item.get('quantity')),
            broken_phones=int(item.get('broken_phones'))
        )
