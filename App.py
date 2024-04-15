#   main application for database
import sqlite3

#   constants
DBNAME = "Jade1.db"
INTWIDTH = 6
STRWIDTH = 20


#   functions

#   show functions


def display_table(results, headings, idname):
    #   displays results from a sql query
    datatype = []
    for cell in results[0]:
        if isinstance(cell, int) or isinstance(cell, float):
            datatype += [INTWIDTH]
        else:
            datatype += [STRWIDTH]
    #   print(datatype)
    for column in range(len(headings)):
        heading = headings[column][0]
        if heading == idname:
            heading = "ID"
        print(heading, (datatype[column] - len(heading)) * " ", end=" | ")
    print()
    for column in range(len(datatype)):
        print((datatype[column] + 1) * "-", end="-+-")
    print()
    for row in results:
        for column in range(len(row)):
            cell = row[column]
            print(cell, (datatype[column] - len(str(cell))) * " ",  end=" | ")
        print()
    for column in range(len(datatype)):
        print((datatype[column] + 1) * "-", end="-+-")
    print()


def show_all_styles():
    #   shows all data in the Furniture table
    db = sqlite3.connect(DBNAME)
    cursor = db.cursor()
    sql = "SELECT * FROM Furniture;"
    cursor.execute(sql)
    results = cursor.fetchall()
    headings = cursor.description
    db.close()
    display_table(results, headings, "ProductID")


def show_all_options():
    #   shows all data in the Options table
    #   changes ProductID to the style's name
    db = sqlite3.connect(DBNAME)
    cursor = db.cursor()
    sql = """SELECT Furniture.Name, Options.Seats, Options.Width,
            Options.Depth, Options.Height, Options.Price
            FROM Options
            LEFT JOIN Furniture
            ON Options.ProductID = Furniture.ProductID;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    headings = cursor.description
    db.close()
    display_table(results, headings, "OptionID")


def show_options_for_style(ProductID):
    #   shows all data from the Options table for a certain ProductID
    db = sqlite3.connect(DBNAME)
    cursor = db.cursor()
    sql = """SELECT OptionID, Seats, Width, Depth, Height, Price
                FROM Options
                WHERE ProductID = %s;""" % ProductID
    cursor.execute(sql)
    results = cursor.fetchall()
    headings = cursor.description
    db.close()
    display_table(results, headings, "OptionID")


def show_all_customers():
    #   shows all data from the Customers table
    db = sqlite3.connect(DBNAME)
    cursor = db.cursor()
    sql = "SELECT * FROM Customers;"
    cursor.execute(sql)
    results = cursor.fetchall()
    headings = cursor.description
    db.close()
    display_table(results, headings, "CustomerID")


def show_all_orders():
    #   shows all data from the orders table
    #   changes CustomerID to the customer's first and last name
    db = sqlite3.connect(DBNAME)
    cursor = db.cursor()
    sql = """SELECT Orders.OrderID, Customers.FirstName, Customers.LastName,
                Furniture.Name, Options.OptionID
                FROM Orders
                LEFT JOIN Customers ON Orders.Customer = Customers.CustomerID
                LEFT JOIN Options ON Orders.Product = Options.OptionID
                LEFT JOIN Furniture ON Options.ProductID =
                Furniture.ProductID;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    headings = cursor.description
    db.close()
    display_table(results, headings, "OrderID")


#   add functions
def add_furniture(name, type):
    #   adds data to Furniture table
    db = sqlite3.connect(DBNAME)
    cursor = db.cursor()
    sql = """INSERT INTO Furniture (Name, Type)
                VALUES ('%s', '%s');""" % (name, type)
    cursor.execute(sql)
    db.commit()


def add_option(product, seats, width, depth, height, price):
    #   adds data to Options table
    db = sqlite3.connect(DBNAME)
    cursor = db.cursor()
    sql = """INSERT INTO Options
                (ProductID, Seats, Width, Depth, Height, Price)
                VALUES ('%s', '%s', '%s', '%s', '%s', '%s');
                """ % (product, seats, width, depth, height, price)
    cursor.execute(sql)
    db.commit()


def add_customer(first, last, address, phone):
    #   adds data to Customers table
    db = sqlite3.connect(DBNAME)
    cursor = db.cursor()
    sql = """INSERT INTO Customers (FirstName, LastName, Address, Phone)
                VALUES ('%s', '%s', '%s', '%s');
                """ % (first, last, address, phone)
    cursor.execute(sql)
    db.commit()


def add_order(customer, product):
    #   adds data to Orders table
    db = sqlite3.connect(DBNAME)
    cursor = db.cursor()
    sql = """INSERT INTO Orders (Customer, Product)
                VALUES ('%s', '%s');""" % (customer, product)
    cursor.execute(sql)
    db.commit()


#   delete functions
def delete_furniture(product):
    #   deletes data from Furniture table
    db = sqlite3.connect(DBNAME)
    cursor = db.cursor()
    sql = """DELETE FROM Furniture WHERE ProductID = %s;""" % product
    cursor.execute(sql)
    db.commit()


def delete_options(option):
    #   deletes data from Options table
    db = sqlite3.connect(DBNAME)
    cursor = db.cursor()
    sql = """DELETE FROM Options WHERE OptionID = %s;""" % option
    cursor.execute(sql)
    db.commit()


def delete_customers(customer):
    #   deletes data from Customers table
    db = sqlite3.connect(DBNAME)
    cursor = db.cursor()
    sql = """DELETE FROM Customers WHERE CustomerID = %s;""" % customer
    cursor.execute(sql)
    db.commit()


def delete_orders(customer, product):
    #   deletes data from Orders table
    db = sqlite3.connect(DBNAME)
    cursor = db.cursor()
    sql = """DELETE FROM Orders WHERE Customer = %s and Product = %s;
            """ % (customer, product)
    cursor.execute(sql)
    db.commit()


#   menu functions
def check_id(idname, table, id):
    #   checks if inputed id exists
    db = sqlite3.connect(DBNAME)
    cursor = db.cursor()
    sql = """SELECT * FROM %s WHERE %s = %s""" % (table, idname, id)
    cursor.execute(sql)
    db.commit()
    results = cursor.fetchall()
    db.close()
    return len(results)


def check_int(prompt):
    #   checks if input is an integer
    while True:
        try:
            num = input("Please enter %s: " % prompt)
            num = int(num)
            break
        except ValueError:
            print("That is not a valid input.")
    return num


def check_float(prompt):
    #   checks if input is a float
    while True:
        try:
            num = input("Please enter %s: " % prompt)
            num = float(num)
            break
        except ValueError:
            print("That is not a valid input.")
    return num


def check_positive(prompt, value):
    #   checks if input is above or equal to zero
    if value == "int":
        while True:
            num = check_int(prompt)
            if num > 0:
                break
            else:
                print("That is not a valid input.")
    elif value == "float":
        while True:
            num = check_float(prompt)
            if num >= 0:
                break
            else:
                print("That is not a valid input.")
    return num


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
                while True:
                    product = input("Please enter an existing product ID: ")
                    check = check_id("ProductID", "Furniture", product)
                    if check > 0:
                        show_options_for_style(product)
                        break
                    else:
                        print("That is not an existing product ID.")

            elif choice2 == "4":
                show_all_customers()

            elif choice2 == "5":
                show_all_orders()

            elif choice2.upper() == "X":
                break

    elif choice1 == "2":
        admincode = "123"
        while True:
            password = input("Please enter admin code or type X to exit: ")
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
                        type = input("Please enter type (chair or suite): ")
                        add_furniture(name, type)
                        print("")
                        print("Here is the updated table: ")
                        show_all_styles()

                    elif choice4 == "2":
                        #   adding data to Options table
                        while True:
                            product = input("Please enter the current product ID: ")
                            check = check_id("ProductID", "Furniture", product)
                            if check > 0:
                                seats = check_positive("number of seats", "float")
                                width = check_positive("width in mm", "int")
                                depth = check_positive("depth in mm", "int")
                                height = check_positive("height in mm", "int")
                                price = check_positive("price", "int")
                                print("")
                                add_option(product, seats, width, depth, height, price)
                                print("Here is the updated table: ")
                                show_all_options()
                                break
                            else:
                                print("That is not an existing product ID.")
                        
                    elif choice4 == "3":
                        #   adding data to Customers table
                        first = input("Please enter customer's first name: ")
                        last = input("Please enter customer's last name: ")
                        address = input("Please enter their address: ")
                        while True:
                            try:
                                phone = input("Please enter phone number: ")
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
                        customer = check_int("an existing customer ID")
                        
                        product = check_int("an existing option ID")
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
                        while True:
                            product = input("Please enter the current product ID: ")
                            check = check_id("ProductID", "Furniture", product)
                            if check > 0:
                                print("")
                                delete_furniture(product)
                                print("Here is the updated table: ")
                                show_all_styles()
                                break
                            else:
                                print("That is not an existing product ID.")

                    elif choice4 == "2":
                        #   deleting data from Options table
                        while True:
                            option = input("Please enter the current option ID: ")
                            check = check_id("ProductID", "Furniture", option)
                            if check > 0:
                                print("")
                                delete_options(option)
                                print("Here is the updated table: ")
                                show_all_options()
                                break
                            else:
                                print("That is not an existing product ID.")

                    elif choice4 == "3":
                        #   deleting data from Customers table
                        customer = input("Please enter the current Customer ID: ")
                        check = check_id("CustomerID", "Customers", customer)
                        if check > 0:
                            print("")
                            delete_customers(customer)
                            print("Here is the updated table: ")
                            show_all_customers()
                            break
                        else:
                            print("That is not an existing product ID.")

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
