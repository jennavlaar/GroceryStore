import sqlite3

connect = sqlite3.connect('grocery.db')
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

#Create users table
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            username text NOT NULL,
            password text NOT NULL,
            name text NOT NULL,
            address text NOT NULL,
            PRIMARY KEY (username)
        )""")

connect.close()

#Convert image into bits to be stored
def cvt_image(fileName):
    with open(fileName, 'rb') as file:
        img_data = file.read()
    return img_data

#Write image to file
def writeToFile(image, fileName):
    with open(fileName, 'wb') as file:
        file.write(image)

#Insert grocery item into groceries table
def insert_item(item_id, item_name, item_img, category, stock, price):
    try:
        connection = sqlite3.connect('grocery.db')
        cursor = connection.cursor()
        insert_query = """ INSERT INTO groceries
                        (item_id, item_name, item_img, category, stock, price) VALUES (?,?,?,?,?,?)"""
        image = cvt_image(item_img)
        data = (item_id, item_name, image, category, stock, price)
        cursor.execute(insert_query, data)
        connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Item ID already exists")
    finally:
        if connection:
            connection.close()
          
#insert UNIQUE user into users table  
def insert_user(username, password, name, address):
    try:
        connection = sqlite3.connect('grocery.db')
        cursor = connection.cursor()
        insert_query = """INSERT INTO users 
                        (username, password, name, address) VALUES (?, ?, ?, ?)"""
        data = (username, password, name, address)
        cursor.execute(insert_query, data)
        connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Username already exists") #prompt user to pick different username
    finally:
        if connection:
            connection.close()

#fetch item from grocery table
def fetch_item(item_id):
    try:
        connection = sqlite3.connect('grocery.db')
        cursor = connection.cursor()
                
        fetch_query = """SELECT * from groceries where item_id = ?"""
        cursor.execute(fetch_query, (item_id,))
        record = cursor.fetchall()

        for row in record:
            name = row[1]
            image = row[2]
            imagePath = name + "1" + ".png"
            writeToFile(image, imagePath) #replace with store on website?
        cursor.close()
  
    except sqlite3.Error as error:
        print("whoopsies fetch")
    finally:
        if connection:
            connection.close()
            
#fetch user from users table
def fetch_item(username):
    try:
        connection = sqlite3.connect('grocery.db')
        cursor = connection.cursor()
                
        fetch_query = """SELECT * from users where username = ?"""
        cursor.execute(fetch_query, (username,))
        record = cursor.fetchall()

        for row in record:
            username = row[0]
            password = row[1]
            name = row[2]
            address = row[3]
        cursor.close()
  
    except sqlite3.Error as error:
        print("whoopsies fetch")
    finally:
        if connection:
            connection.close()


#test inserts/fetches
insert_item(1,"Bread", "images/bread.png", "Food", 12, 2.97)
fetch_item(1)
insert_user("john", "pass1", "john", "123 john st")
insert_user("john", "pass1", "john", "123 john st")

