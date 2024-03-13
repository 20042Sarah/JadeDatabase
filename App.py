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
    sql = """SELECT Furniture.Name, Options.Seats, Options.Width, Options.Depth, Options.Height, Options.Price 
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

#   menu
while True:
    choice = input("Press 1 to show all styles, press 2 to show all options, press 3 to show all options for a style, press 4 to show all customers, press X to exit: ")

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

    elif choice.lower() == "x":
        break
