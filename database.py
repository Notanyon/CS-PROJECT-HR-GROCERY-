import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aditya2009",
    database="grocery_db"
)

cursor = conn.cursor()


def add_item(item, quantity):
    cursor.execute(
        "INSERT INTO grocery_list(item, quantity) VALUES(%s,%s)",
        (item, quantity)
    )
    conn.commit()


def get_items():
    cursor.execute("SELECT * FROM grocery_list")
    return cursor.fetchall()


def delete_item(item_id):
    cursor.execute(
        "DELETE FROM grocery_list WHERE id=%s",
        (item_id,)
    )
    conn.commit()


def clear_items():
    cursor.execute("DELETE FROM grocery_list")
    conn.commit()