from tkinter import *
from tkinter import messagebox
from database import *

window = Tk()
window.title("Grocery List Manager")
window.geometry("800x600")
window.resizable(False, False)

# ---------------- TITLE ----------------

Label(
    window,
    text="GROCERY LIST MANAGER",
    font=("Arial", 18, "bold")
).pack(pady=15)

groceries = [
    "Milk", "Bread", "Eggs", "Rice", "Flour", "Sugar",
    "Salt", "Cooking Oil", "Butter", "Cheese",
    "Chicken", "Fish", "Tomatoes", "Potatoes",
    "Onions", "Apples", "Bananas", "Oranges",
    "Tea", "Coffee", "Soap", "Shampoo"
]

# ---------------- MAIN AREA ----------------

main_frame = Frame(window)
main_frame.pack()

# ---------- LEFT ----------

left_frame = Frame(main_frame)
left_frame.grid(row=0, column=0, padx=20)

Label(
    left_frame,
    text="Available Groceries",
    font=("Arial", 11, "bold")
).pack()

grocery_frame = Frame(left_frame)
grocery_frame.pack()

grocery_scroll = Scrollbar(grocery_frame)

grocery_list = Listbox(
    grocery_frame,
    width=25,
    height=14,
    selectmode=MULTIPLE,
    exportselection=False,
    yscrollcommand=grocery_scroll.set
)

grocery_scroll.config(command=grocery_list.yview)

grocery_list.pack(side=LEFT)
grocery_scroll.pack(side=RIGHT, fill=Y)

for item in groceries:
    grocery_list.insert(END, item)

# ---------- MIDDLE ----------

middle_frame = Frame(main_frame)
middle_frame.grid(row=0, column=1, padx=25)

Label(
    middle_frame,
    text="Quantity",
    font=("Arial", 11)
).pack()

quantity_entry = Entry(
    middle_frame,
    width=10,
    justify="center"
)
quantity_entry.pack(pady=8)

# ---------- RIGHT ----------

right_frame = Frame(main_frame)
right_frame.grid(row=0, column=2, padx=20)

Label(
    right_frame,
    text="Shopping Cart",
    font=("Arial", 11, "bold")
).pack()

cart_frame = Frame(right_frame)
cart_frame.pack()

cart_scroll = Scrollbar(cart_frame)

cart = Listbox(
    cart_frame,
    width=35,
    height=14,
    yscrollcommand=cart_scroll.set
)

cart_scroll.config(command=cart.yview)

cart.pack(side=LEFT)
cart_scroll.pack(side=RIGHT, fill=Y)

# ---------------- FUNCTIONS ----------------

def refresh_cart():

    cart.delete(0, END)

    items = get_items()

    for number, item in enumerate(items, start=1):

        cart.insert(
            END,
            f"{number}. {item[1]} (Qty: {item[2]})"
        )


def add_items():

    selected = grocery_list.curselection()

    if len(selected) == 0:
        messagebox.showwarning(
            "Warning",
            "Please select grocery items."
        )
        return

    qty = quantity_entry.get().strip()

    if qty == "":
        messagebox.showwarning(
            "Warning",
            "Enter quantity."
        )
        return

    try:
        qty = int(qty)
    except:
        messagebox.showerror(
            "Error",
            "Quantity must be a number."
        )
        return

    for index in selected:
        add_item(groceries[index], qty)

    quantity_entry.delete(0, END)

    refresh_cart()


def delete_selected():

    try:

        selected = cart.get(ACTIVE)

        item_number = int(selected.split(".")[0])

        items = get_items()

        delete_item(items[item_number - 1][0])

        refresh_cart()

    except:

        messagebox.showerror(
            "Error",
            "Please select an item."
        )


def clear_list():

    if messagebox.askyesno(
        "Confirm",
        "Clear the entire shopping list?"
    ):

        clear_items()

        refresh_cart()

# ---------------- ADD BUTTON ----------------

Button(
    window,
    text="Add Selected Items",
    width=22,
    command=add_items
).pack(pady=15)

# ---------------- ACTION BUTTONS ----------------

button_frame = Frame(window)
button_frame.pack()

Button(
    button_frame,
    text="Delete Item",
    width=18,
    command=delete_selected
).grid(row=0, column=0, padx=15)

Button(
    button_frame,
    text="Clear Shopping List",
    width=18,
    command=clear_list
).grid(row=0, column=1, padx=15)

refresh_cart()

window.mainloop()
