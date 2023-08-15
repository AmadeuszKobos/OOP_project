import csv
from Item import Item
from Phone import Phone
from Laptop import Laptop
from tkinter import ttk
from tkinter import filedialog
import customtkinter as ctk


def items_names():
    return [item.name for item in Item.all_items]


def color(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"


def encounter_problem(text):
    return color(text, "31")


def create_object(item, item_type, name, names_list):
    if item_type == 'Phone' and name not in names_list:  # if object is Phone and doesn't exist yet
        Phone.initiate_from_csv(item=item)
    elif item_type == 'Laptop' and name not in names_list:  # if object is Laptop and doesn't exist yet
        Laptop.initiate_from_csv(item=item)
    else:
        print("Some problem with creating an object")


def from_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        items = list(reader)

        for row_number, item in enumerate(items, start=1):  # numerate number to see in case of exception incorrect row
            obj_type = item.get('object_type')              # get the type of the object to create
            obj_name = item.get('name')                     # get the name of object to create
            names_taken = items_names()                     # get list of names already taken

            create_object(item=item, item_type=obj_type, name=obj_name, names_list=names_taken)


def print_all_objects():
    obj_table = ttk.Treeview(master=app, columns=("Type", "Name", "Price", "Quantity"), show="headings")
    obj_table.heading("Type", text="Type")
    obj_table.heading("Name", text="Name")
    obj_table.heading("Price", text="Price")
    obj_table.heading("Quantity", text="Quantity")

    table_style = ttk.Style()
    table_style.configure("Custom.Treeview", background="#333", foreground="white")

    obj_table.configure(style="Custom.Treeview")  # setting style to "Table Style" defined below
    obj_table.pack(pady=20)

    for item in Item.all_items:
        Item.print_object(item, table=obj_table)


def open_file_dialog():
    try:
        file_path = filedialog.askopenfilename(title="Choose file", filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        current_file_label.configure(text=f"Current file path: {file_path}")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Exception during opening file")
    else:
        create_objects_button.pack()
        from_csv(file_path)


if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry('800x600')
    app.title('Create objects from file')

    choose_csv_button = ctk.CTkButton(master=app, text="Choose CSV file", command=open_file_dialog)
    choose_csv_button.pack(pady=10)

    current_file_label = ctk.CTkLabel(master=app, text="Current file: ")
    current_file_label.pack(pady=0)

    create_objects_button = ctk.CTkButton(master=app, text="Create objects with file", command=print_all_objects)

    app.mainloop()









