import csv
from Item import Item
from Phone import Phone
from Laptop import Laptop


def items_names():
    return [item.name for item in Item.all_items]


def color(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"


def encounter_problem(text):
    return color(text, "31")


def from_csv():
    with open('items.csv', 'r') as f:
        reader = csv.DictReader(f)
        items = list(reader)

        for row_number, item in enumerate(items, start=1):
            obj_type = item.get('object_type')
            obj_name = item.get('name')
            if obj_type == 'Phone' and obj_name not in items_names():
                Phone.initiate_from_csv(item=item)
            elif obj_type == 'Laptop' and obj_name not in items_names():
                Laptop.initiate_from_csv(item=item)
            else:
                print(encounter_problem(f"Wrong values in line {row_number}."))


if __name__ == "__main__":
    from_csv()

# print(Item.all_items)




# print(color(Item.is_integer(5.0), "34"))



