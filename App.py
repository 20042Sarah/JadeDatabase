#   main application for database
import sqlite3


#   functions
dbname = "Jade1.db"

#   show functions
def show_all_styles():
    #   shows all data in the Furniture table
    db = sqlite3.connect(dbname)
    cursor = db.cursor()
    sql = "SELECT * FROM Furniture;"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    print("FURNITURE TABLE")
    for i in results:
        print(i[0], i[1], i[2])


def show_all_options():
    #   shows all data in the Options table
    #   changes ProductID to the style's name
    db = sqlite3.connect(dbname)
    cursor = db.cursor()
    sql = """SELECT Furniture.Name, Options.Seats, Options.Width,
            Options.Depth, Options.Height, Options.Price
            FROM Options
            LEFT JOIN Furniture
            ON Options.Product_ID = Furniture.Product_ID;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    print("OPTIONS TABLE")
    for i in results:
        print(i[0], i[1], i[2], i[3], i[4], i[5])


def show_options_for_style(Product_ID):
    #   shows all data from the Options table for a certain ProductID
    db = sqlite3.connect(dbname)
    cursor = db.cursor()
    sql = """SELECT Option_ID, Seats, Width, Depth, Height, Price
                FROM Options
                WHERE Product_ID = %s;""" % Product_ID
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    for i in results:
        print(i[0], i[1], i[2], i[3], i[4], i[5])


def show_all_customers():
    #   shows all data from the Customers table
    db = sqlite3.connect(dbname)
    cursor = db.cursor()
    sql = "SELECT * FROM Customers;"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    print("CUSTOMERS TABLE")
    for i in results:
        print(i[0], i[1], i[2], i[3], i[4])


def show_all_orders():
    #   shows all data from the orders table
    #   changes CustomerID to the customer's first and last name
    db = sqlite3.connect(dbname)
    cursor = db.cursor()
    sql = """SELECT Customers.FirstName, Customers.LastName, Furniture.Name,
                Options.Option_ID
                FROM Orders
                LEFT JOIN Customers ON Orders.Customer = Customers.CustomerID
                LEFT JOIN Options ON Orders.Product = Options.Option_ID
                LEFT JOIN Furniture ON Options.Product_ID =
                Furniture.Product_ID;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    print("ORDERS TABLE")
    for i in results:
        print(i[0], i[1], i[2], i[3])


#   add functions
def add_furniture(name, type):
    #   adds data to Furniture table
    db = sqlite3.connect(dbname)
    cursor = db.cursor()
    sql = """INSERT INTO Furniture (Name, Type)
                VALUES ('%s', '%s');""" % (name, type)
    cursor.execute(sql)
    db.commit()


def add_option(product, seats, width, depth, height, price):
    #   adds data to Options table
    db = sqlite3.connect(dbname)
    cursor = db.cursor()
    sql = """INSERT INTO Options
                (Product_ID, Seats, Width, Depth, Height, Price)
                VALUES ('%s', '%s', '%s', '%s', '%s', '%s');
                """ % (product, seats, width, depth, height, price)
    cursor.execute(sql)
    db.commit()


def add_customer(first, last, address, phone):
    #   adds data to Customers table
    db = sqlite3.connect(dbname)
    cursor = db.cursor()
    sql = """INSERT INTO Customers (FirstName, LastName, Address, Phone)
                VALUES ('%s', '%s', '%s', '%s');
                """ % (first, last, address, phone)
    cursor.execute(sql)
    db.commit()


def add_order(customer, product):
    #   adds data to Orders table
    db = sqlite3.connect(dbname)
    cursor = db.cursor()
    sql = """INSERT INTO Orders (Customer, Product)
                VALUES ('%s', '%s');""" % (customer, product)
    cursor.execute(sql)
    db.commit()


#   delete functions
def delete_furniture(product):
    #   deletes data from Furniture table
    db = sqlite3.connect(dbname)
    cursor = db.cursor()
    sql = """DELETE FROM Furniture WHERE Product_ID = %s;""" % product
    cursor.execute(sql)
    db.commit()


def delete_options(option):
    #   deletes data from Options table
    db = sqlite3.connect(dbname)
    cursor = db.cursor()
    sql = """DELETE FROM Options WHERE Option_ID = %s;""" % option
    cursor.execute(sql)
    db.commit()


def delete_customers(customer):
    #   deletes data from Customers table
    db = sqlite3.connect(dbname)
    cursor = db.cursor()
    sql = """DELETE FROM Customers WHERE CustomerID = %s;""" % customer
    cursor.execute(sql)
    db.commit()


def delete_orders(customer, product):
    #   deletes data from Orders table
    db = sqlite3.connect(dbname)
    cursor = db.cursor()
    sql = """DELETE FROM Orders WHERE Customer = %s and Product = %s;
            """ % (customer, product)
    cursor.execute(sql)
    db.commit()


#   menu functions
def check_ids(idname, table, id):
    db = sqlite3.connect(dbname)
    cursor = db.cursor()
    sql = """SELECT %s FROM %s""" % (idname, table)
    cursor.execute(sql)
    db.commit()
    results = cursor.fetchall()
    db.close()

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
                show_all_styles()

            elif choice2 == "2":
                show_all_options()

            elif choice2 == "3":
                product = input("Please type an existing product ID: ")
                show_options_for_style(product)

            elif choice2 == "4":
                show_all_customers()

            elif choice2 == "5":
                show_all_orders()

            elif choice2.upper() == "X":
                break

    elif choice1 == "2":
        admincode = "123"
        while True:
            password = input("Please enter admin code to continue or type X to exit: ")
            if password == admincode:
                break
            elif password.upper() == "X":
                break
            else:
                print("That is not the admin code")

        while True:
            if password.upper() == "X":
                break

            #   edit data menu
            choice3 = input("""
    Press 1 to add data,
    Press 2 to delete data,
    or press X to exit: """)
            print("")

            if choice3 == "1":
                #   add data menu
                while True:
                    choice4 = input("""
    Press 1 to add data to Furniture table,
    Press 2 to add data to Options table,
    Press 3 to add data to Customer table,
    Press 4 to add data to Orders table,
    or press X to exit: """)
                    print("")
                    if choice4 == "1":
                        #   adding data to Furniture table
                        name = input("Please enter the new name: ")
                        type = input("Please enter type (e.g. chair or suite): ")
                        add_furniture(name, type)
                        print("")
                        print("Here is the updated table: ")
                        show_all_styles()

                    elif choice4 == "2":
                        #   adding data to Options table
                        while True:
                            #   could try and check that product id exists
                            try:
                                product = input("Please enter existing Product ID: ")
                                product = int(product)
                                break
                            except ValueError:
                                print("That is not a valid input.")
                        while True:
                            try:
                                seats = input("Please enter number of seats: ")
                                seats = float(seats)
                                break
                            except ValueError:
                                print("That is not a valid input.")
                        while True:
                            try:
                                width = int(input("Please enter width in mm: "))
                                break
                            except ValueError:
                                print("That is not a valid input.")
                        while True:
                            try:
                                depth = int(input("Please enter depth in mm: "))
                                break
                            except ValueError:
                                print("That is not a valid input.")
                        while True:
                            try:
                                height = int(input("Please enter height in mm: "))
                                break
                            except ValueError:
                                print("That is not a valid input.")
                        while True:
                            try:
                                price = int(input("Please enter price: "))
                                break
                            except ValueError:
                                print("That is not a valid input.")
                        print("")
                        add_option(product, seats, width, depth, height, price)
                        print("Here is the updated table: ")
                        show_all_options()

                    elif choice4 == "3":
                        #   adding data to Customers table
                        first = input("Please enter new customer's first name: ")
                        last = input("Please enter new customer's last name: ")
                        address = input("Please enter their address: ")
                        while True:
                            try:
                                phone = input("Please enter their phone number: ")
                                check = int(phone)
                                break
                            except ValueError:
                                print("That is not a valid input.")
                        print("")
                        add_customer(first, last, address, phone)
                        print("Here is the updated table: ")
                        show_all_customers()

                    elif choice4 == "4":
                        #   adding data to Orders table
                        while True:
                            try:
                                customer = input("Please enter existing Customer ID: ")
                                customer = int(customer)
                                break
                            except ValueError:
                                print("That is not a valid input.")
                        while True:
                            try:
                                product = input("Please enter existing Option ID: ")
                                product = int(product)
                                break
                            except ValueError:
                                print("That is not a valid input.")
                        print("")
                        add_order(customer, product)
                        print("Here is the updated table: ")
                        show_all_orders()

                    elif choice4.upper() == "X":
                        break

            elif choice3 == "2":
                #   delete data menu
                while True:
                    choice4 = input("""
    Press 1 to delete data from Furniture table,
    Press 2 to delete data from Options table,
    Press 3 to delete data from Customer table,
    Press 4 to delete data from Orders table,
    or press X to exit: """)
                    print("")

                    if choice4 == "1":
                        #   deleting data from Furniture table
                        product = input("Please enter the current Product ID: ")
                        print("")
                        delete_furniture(product)
                        print("Here is the updated table: ")
                        show_all_styles()

                    elif choice4 == "2":
                        #   deleting data from Options table
                        option = input("Please enter the current Option ID: ")
                        print("")
                        delete_options(option)
                        print("Here is the updated table: ")
                        show_all_options()

                    elif choice4 == "3":
                        #   deleting data from Customers table
                        customer = input("Please enter the current Customer ID: ")
                        print("")
                        delete_customers(customer)
                        print("Here is the updated table: ")
                        show_all_customers()

                    elif choice4 == "4":
                        #   deleting data from Orders table
                        customer = input("Please enter the current Customer ID: ")
                        product = input("Please enter the current Option ID: ")
                        print("")
                        delete_orders(customer, product)
                        print("Here is the updated table: ")
                        show_all_orders()

                    elif choice4.upper() == "X":
                        break

            elif choice3.upper() == "X":
                break

    elif choice1.upper() == "X":
        break
