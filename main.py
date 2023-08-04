import csv
from Item import Item
from Phone import Phone
from Laptop import Laptop
import customtkinter as ctk


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

        for row_number, item in enumerate(items, start=1): # numerate number to see in case of exception incorrect row
            obj_type = item.get('object_type')
            obj_name = item.get('name')
            names_taken = items_names()
            if obj_type == 'Phone' and obj_name not in names_taken: # if object is Phone and doesn't exist yet
                Phone.initiate_from_csv(item=item)
            elif obj_type == 'Laptop' and obj_name not in names_taken: # if object is Laptop and doesn't exist yet
                Laptop.initiate_from_csv(item=item)
            else:
                print(encounter_problem(f"Wrong values in line {row_number}.")) # if there is no such type or object already exist


def print_all_objects():
    for item in Item.all_items:
        Phone.print_object(item, table=obj_table)


if __name__ == "__main__":
    from_csv()
    app = ctk.CTk()
    app.geometry('800x600')
    app.title('Create objects from file')

    # obj_list = ctk.CTkFrame(master=app)

    obj_table = ctk.CTkTabview(master=app)
    obj_table.pack()
    obj_table.add("Type")
    obj_table.add("Name")
    obj_table.add("Price")
    obj_table.add("Quantity")

    print_all_objects()

    app.mainloop()

# print(Item.all_items)



