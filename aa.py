import tkinter as tk
from tkinter import messagebox

def show_message(item_name):
    messagebox.showinfo("Selected Item", f"You selected: {item_name}")

def create_menu_items(menu, items):
    for item_name, item_commands in items.items():
        sub_menu = tk.Menu(menu, tearoff=0)
        for command_name, command_func in item_commands.items():
            sub_menu.add_command(label=command_name, command=lambda cmd=command_func: show_message(cmd))
        menu.add_cascade(label=item_name, menu=sub_menu)

# Ana Tkinter penceresi oluşturma
root = tk.Tk()
root.title("Menu Example")

# Sol taraftaki menü çerçevesi
menu_frame = tk.Frame(root, bg="lightgray")
menu_frame.pack(side="left", fill="y")

# Kategori ve öğeler
menu_items = {
    "Category 1": {
        "Item 1-1": "Item 1-1",
        "Item 1-2": "Item 1-2",
        "Item 1-3": "Item 1-3"
    },
    "Category 2": {
        "Item 2-1": "Item 2-1",
        "Item 2-2": "Item 2-2",
        "Item 2-3": "Item 2-3"
    },
    "Category 3": {
        "Item 3-1": "Item 3-1",
        "Item 3-2": "Item 3-2",
        "Item 3-3": "Item 3-3"
    }
}

# Menü öğelerini oluşturma
create_menu_items(tk.Menu(menu_frame), menu_items)

root.mainloop()
