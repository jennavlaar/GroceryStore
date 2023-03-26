from django.db import models

# Create your models here.
import sqlite3

class Grocery:
        
    connect = sqlite3.connect('grocery.sqlite3')
    cursor = connect.cursor()


    #Create groceries table
    cursor.execute("""CREATE TABLE IF NOT EXISTS groceries (
                item_id integer NOT NULL,
                item_name text NOT NULL,
                item_img blob NOT NULL,
                category text NOT NULL,
                stock integer NOT NULL,
                price real NOT NULL,
                PRIMARY KEY (item_id)
            )""")

    #Create user table
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                username text NOT NULL UNIQUE,
                PRIMARY KEY (username)
            )""")

    #Create registered registered user table
    cursor.execute("""CREATE TABLE IF NOT EXISTS registeredusers(
                username text NOT NULL UNIQUE,
                password text NOT NULL,
                name text NOT NULL,
                address text NOT NULL,
                FOREIGN KEY (username) REFERENCES users(username)
            )""")

    #Create admin user table
    cursor.execute("""CREATE TABLE IF NOT EXISTS admin(
                admin_id integer NOT NULL,
                username text NOT NULL,
                password text NOT NULL,
                name text NOT NULL,
                address text NOT NULL,
                PRIMARY KEY (admin_id),
                FOREIGN KEY (username) REFERENCES users(username)
            )""")

    #Create order table
    cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
                order_id integer NOT NULL,
                username text NOT NULL,
                address text NOT NULL,
                PRIMARY KEY (order_id),
                FOREIGN KEY (username) REFERENCES users(username)
            )""")

    #Create receipt table
    cursor.execute("""CREATE TABLE IF NOT EXISTS receipt(
                order_id integer NOT NULL,
                total real NOT NULL,
                PRIMARY KEY (order_id),
                FOREIGN KEY (order_id) REFERENCES orders(order_id)
            )""")

    #Create cart table
    cursor.execute("""CREATE TABLE IF NOT EXISTS cart(
                contents blob NOT NULL,
                user_id text NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(username)
                FOREIGN KEY (contents) REFERENCES groceries(item_id)
            )""")

    #Create employee table
    cursor.execute("""CREATE TABLE IF NOT EXISTS employees(
                employee_id integer NOT NULL,
                first_name text NOT NULL,
                last_name text NOT NULL,
                employer text NOT NULL,
                PRIMARY KEY (employee_id)
                FOREIGN KEY (employer) REFERENCES supplier(name)
            )""")

    #Create supplier table
    cursor.execute("""CREATE TABLE IF NOT EXISTS suppliers(
                supplier_name text NOT NULL,
                product text NOT NULL,
                PRIMARY KEY (supplier_name)
                FOREIGN KEY (product) REFERENCES product(product_name)
            )""")

    #Create product table
    cursor.execute("""CREATE TABLE IF NOT EXISTS product(
                product_name text NOT NULL,
                stock int NOT NULL,
                PRIMARY KEY (product_name)
            )""")

    #Create product table
    cursor.execute("""CREATE TABLE IF NOT EXISTS supplies(
                supplier text NOT NULL,
                grocery_item text NOT NULL,
                FOREIGN KEY (supplier) REFERENCES suppliers(supplier_name)
                FOREIGN KEY (grocery_item) REFERENCES groceries(item_id)
            )""")

    #Create farm table
    cursor.execute("""CREATE TABLE IF NOT EXISTS farm(
                farm_name text NOT NULL,
                location text NOT NULL,
                PRIMARY KEY (farm_name)
            )""")

    #Create sells to table
    cursor.execute("""CREATE TABLE IF NOT EXISTS sellsto(
                farm_name text NOT NULL,
                supplier text NOT NULL,
                FOREIGN KEY (supplier) REFERENCES suppliers(supplier_name)
                FOREIGN KEY (farm_name) REFERENCES farm(farm_name)
            )""")



    connect.close()
