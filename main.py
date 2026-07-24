from tkinter import *
from tkinter import messagebox
from database import *

window = Tk()
window.title("Grocery List Manager")
window.geometry("800x550")
window.resizable(False, False)

Label(
    window,
    text="GROCERY LIST MANAGER",
    font=("Arial", 18, "bold")
).pack(pady=10)

groceries = [
    "Milk","Bread","Eggs","Rice","Flour","Sugar","Salt",
    "Cooking Oil","Butter","Cheese","Chicken","Fish",
    "Tomatoes","Potatoes","Onions","Apples","Bananas",
    "Oranges","Tea","Coffee","Soap","Shampoo"
]

main_frame = Frame(window)
main_frame.pack(pady=10)

# ---------------- LEFT SIDE ----------------

left_frame = Frame(main_frame)
left_frame.grid(row=0, column=0, padx=15)

Label(
    left_frame,
    text="Available Groceries",
    font=("Arial",11,"bold")
).pack()

grocery_frame = Frame(left_frame)
grocery_frame.pack()

grocery_scroll = Scrollbar(grocery_frame)

grocery_list = Listbox(
    grocery_frame,
    selectmode=MULTIPLE,
    width=25,
    height=15,
    exportselection=False,
    yscrollcommand=grocery_scroll.set
)

grocery_scroll.config(command=grocery_list.yview)

grocery_scroll.pack(side=RIGHT, fill=Y)
grocery_list.pack(side=LEFT)

for item in groceries:
    grocery_list.insert(END,item)

# ---------------- MIDDLE ----------------

middle_frame = Frame(main_frame)
middle_frame.grid(row=0,column=1,padx=20)

Label(
    middle_frame,
    text="Quantity",
    font=("Arial",11,"bold")
).pack()

quantity_entry = Entry(
    middle_frame,
    width=10,
    justify="center"
)
quantity_entry.pack(pady=10)

# ---------------- RIGHT SIDE ----------------

right_frame = Frame(main_frame)
right_frame.grid(row=0,column=2,padx=15)

Label(
    right_frame,
    text="Shopping Cart",
    font=("Arial",11,"bold")
).pack()

cart_frame = Frame(right_frame)
cart_frame.pack()

cart_scroll = Scrollbar(cart_frame)

cart = Listbox(
    cart_frame,
    width=35,
    height=15,
    yscrollcommand=cart_scroll.set
)

cart_scroll.config(command=cart.yview)

cart_scroll.pack(side=RIGHT, fill=Y)
cart.pack(side=LEFT)

# ---------------- FUNCTIONS ----------------

def refresh_cart():

    cart.delete(0,END)

    items = get_items()

    for item in items:
        cart.insert(
            END,
            f"{item[0]} | {item[1]} | Qty: {item[2]}"
        )


def add_items():

    selected = grocery_list.curselection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select grocery items."
        )
        return

    qty = quantity_entry.get()

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
        add_item(groceries[index],qty)

    quantity_entry.delete(0,END)

    refresh_cart()


def delete_selected():

    try:
        selected = cart.get(ACTIVE)

        item_id = selected.split("|")[0].strip()

        delete_item(item_id)

        refresh_cart()

    except:
        messagebox.showerror(
            "Error",
            "Select an item to delete."
        )


def clear_list():

    answer = messagebox.askyesno(
        "Confirm",
        "Clear entire shopping list?"
    )

    if answer:
        clear_items()
        refresh_cart()

# ---------------- BUTTONS ----------------

button_frame = Frame(window)
button_frame.pack(pady=20)

Button(
    button_frame,
    text="Add Selected",
    width=15,
    command=add_items
).grid(row=0,column=0,padx=10)

Button(
    button_frame,
    text="Delete Item",
    width=15,
    command=delete_selected
).grid(row=0,column=1,padx=10)

Button(
    button_frame,
    text="Clear List",
    width=15,
    command=clear_list
).grid(row=0,column=2,padx=10)

Button(
    button_frame,
    text="Refresh",
    width=15,
    command=refresh_cart
).grid(row=0,column=3,padx=10)

refresh_cart()

window.mainloop()