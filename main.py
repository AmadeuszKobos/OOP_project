import csv
from Item import Item
from Phone import Phone


def color(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"


def from_csv():
    with open('items.csv', 'r') as f:
        reader = csv.DictReader(f)
        items = list(reader)

        for item in items:
            obj_type = item.get('object_type')
            if obj_type == 'Phone':
                Phone.initiate_from_csv(item=item)
            else:
                Item.initiate_from_csv(item=item)


if __name__ == "__main__":
    from_csv()

print(Item.all_items)

# print(color(Item.is_integer(5.0), "34"))



