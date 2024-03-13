#   main application for database
import sqlite3


#   functions
def show_all_styles():
    #   shows all data in the Furniture table
    db = sqlite3.connect("Jade1.db")
    cursor = db.cursor()
    sql = "SELECT * FROM Furniture;"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results


def show_all_options():
    #   shows all data in the Options table
    #   changes ProductID to the style's name
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
    #   shows all data from the Options table for a certain ProductID
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
    #   shows all data from the Customers table
    db = sqlite3.connect("Jade1.db")
    cursor = db.cursor()
    sql = "SELECT * FROM Customers;"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results


def show_all_orders():
    #   shows all data from the orders table
    #   changes CustomerID to the customer's first and last name
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
    #   first menu
    choice1 = input("""
    Press 1 to view data,
    Press 2 to edit data,
    or press X to exit: """)
    print("")

    if choice1 == "1":
        while True:
            #   viewing menu
            choice2 = input("""
    Press 1 to view all styles,
    Press 2 to view all options,
    Press 3 to view all options for a style,
    Press 4 to view all customers,
    Press 5 to view all orders,
    or press X to exit: """)
            print("")

            if choice2 == "1":
                results = show_all_styles()
                for i in results:
                    print(i[0], i[1], i[2])

            elif choice2 == "2":
                results = show_all_options()
                for i in results:
                    print(i[0], i[1], i[2], i[3], i[4], i[5])

            elif choice2 == "3":
                product = input("Please type product ID: ")
                results = show_options_for_style(product)
                for i in results:
                    print(i[0], i[1], i[2], i[3], i[4], i[5])

            elif choice2 == "4":
                results = show_all_customers()
                for i in results:
                    print(i[0], i[1], i[2], i[3], i[4])

            elif choice2 == "5":
                results = show_all_orders()
                for i in results:
                    print(i[0], i[1], i[2])

            elif choice2.lower() == "x":
                break

    if choice1 == "2":
        admincode = "123"
        while True:
            password = input("Please enter admin code to contiue: ")
            if password == admincode:
                break
            else:
                print("That is not the admin coede")

        while True:
            #   edit data menu
            choice3 = input("""
    Press 1 to add data,
    Press 2 to delete data,
    or press X to exit: """)
            print("")

            if choice3 == "1":
                #   needs work
                print("This is currently unavailable")

            elif choice3 == "2":
                #   needs work
                print("This is currently unavailable")

            elif choice3.lower() == "x":
                break

    elif choice1.lower() == "x":
        break
