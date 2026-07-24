# Grocery List Manager

## Overview

The Grocery List Manager is a desktop application developed using Python and MySQL. It allows users to create and manage a shopping list for grocery trips. Users can select multiple grocery items, specify the quantity, and store the shopping list in a MySQL database. The application uses a graphical user interface (GUI) built with Tkinter.

---

## Features

- Select multiple grocery items at once
- Enter quantity for selected items
- Add items to the shopping cart
- View all grocery items in the cart
- Delete selected items
- Clear the entire shopping list
- Stores data permanently in a MySQL database

---

## Technologies Used

- Python 3
- Tkinter
- MySQL
- mysql-connector-python

---

## Database

### Database Name

```
grocery_db
```

### Table Name

```
grocery_list
```

### Table Structure

| Column | Type |
|----------|---------|
| id | INT (Primary Key, Auto Increment) |
| item | VARCHAR(100) |
| quantity | INT |

---

## Installation

1. Install Python 3.
2. Install MySQL Server and MySQL Workbench.
3. Install the required Python package:

```bash
pip install mysql-connector-python
```

4. Create the database:

```sql
CREATE DATABASE grocery_db;

USE grocery_db;

CREATE TABLE grocery_list(
    id INT AUTO_INCREMENT PRIMARY KEY,
    item VARCHAR(100),
    quantity INT
);
```

5. Open `database.py` and update the MySQL password:

```python
password = "YOUR_PASSWORD"
```

6. Run the application:

```bash
python main.py
```

---

## Project Files

```
Grocery List Manager/

│── main.py
│── database.py
│── README.md
```

---

## How to Use

1. Select one or more grocery items from the available list.
2. Enter the required quantity.
3. Click **Add Selected** to add the items to the shopping cart.
4. View all added items in the shopping cart.
5. Select an item from the cart and click **Delete Item** to remove it.
6. Click **Clear List** to remove all items from the shopping cart.

---

## Future Improvements

- Add item categories (Fruits, Vegetables, Dairy, etc.)
- Edit the quantity of existing items
- Search for grocery items
- Calculate the total estimated cost
- Add a dark mode interface
- Print or export the shopping list

---

## END
