#   main application for database
import sqlite3


#   functions
def show_all_styles():
    db = sqlite3.connect("Jade1.db")
    cursor = db.cursor()
    sql = "SELECT * FROM Furniture;"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results


def show_all_options():
    db = sqlite3.connect("Jade1.db")
    cursor = db.cursor()
    sql = """SELECT Furniture.Name, Options.Seats, Options.Width,
            Options.Depth, Options.Height, Options.Price
            FROM Options
            LEFT JOIN Furniture
            ON Options.Product_ID = Furniture.Product_ID;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results


def show_options_for_style(Product_ID):
    db = sqlite3.connect("Jade1.db")
    cursor = db.cursor()
    sql = """SELECT Option_ID, Seats, Width, Depth, Height, Price
                FROM Options
                WHERE Product_ID = %s;""" % Product_ID
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results


def show_all_customers():
    db = sqlite3.connect("Jade1.db")
    cursor = db.cursor()
    sql = "SELECT * FROM Customers;"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results


def show_all_orders():
    db = sqlite3.connect("Jade1.db")
    cursor = db.cursor()
    sql = """SELECT Customers.FirstName, Customers.LastName, Orders.Product
                FROM Orders
                LEFT JOIN Customers ON Orders.Customer = Customers.CustomerID;
                """
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results


#   menu
print("Welcome to the Jade Furniture Database.")
while True:
    choice = input("""
    Press 1 to view all styles,
    Press 2 to view all options,
    Press 3 to view all options for a style,
    Press 4 to view all customers,
    Press 5 to view all orders,
    or press X to exit: """)
    print("")

    if choice == "1":
        results = show_all_styles()
        print(results)

    elif choice == "2":
        results = show_all_options()
        print(results)

    elif choice == "3":
        product = input("Please type product ID: ")
        results = show_options_for_style(product)
        print(results)

    elif choice == "4":
        results = show_all_customers()
        print(results)

    elif choice == "5":
        results = show_all_orders()
        print(results)

    elif choice.lower() == "x":
        break
