import mysql.connector
from mysql.connector import Error
from faker import Faker
import random

def create_connection():
    """ Create a database connection to a MySQL database """
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='storage_db',  # Thay đổi tên cơ sở dữ liệu nếu cần
            user='root',  # Thay đổi tên người dùng nếu cần
            password=''  # Thay đổi mật khẩu nếu cần
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def close_connection(connection):
    if connection and connection.is_connected():
        connection.close()
        print("The connection is closed")

def create_fake_data():
    fake = Faker()
    connection = create_connection()
    if connection is None:
        return

    cursor = connection.cursor()

    try:
        # Insert fake users
        for _ in range(50):
            username = fake.user_name()
            password = fake.password()
            address = fake.address().replace('\n', ', ')
            phone = fake.phone_number()
            email = fake.email()
            cursor.execute("INSERT INTO user (username, password, address, phone, email) VALUES (%s, %s, %s, %s, %s)", 
                           (username, password, address, phone, email))

        # Insert fake categories
        categories = ['Laptop', 'Điện thoại', 'Phụ kiện', 'Đòng hồ', 'Smartwatch', 'Tablet']
        for category in categories:
            cursor.execute("INSERT INTO category (name) VALUES (%s)", (category,))

        # Insert fake products
        # cursor.execute("SELECT id FROM category")
        # category_ids = [row[0] for row in cursor.fetchall()]
        
        # for _ in range(100):
        #     name = fake.word().capitalize()
        #     price = round(random.uniform(10.0, 1000.0), 2)
        #     quantity = random.randint(1, 100)
        #     category_id = random.choice(category_ids)
        #     cursor.execute("INSERT INTO product (name, price, quantity, category_id) VALUES (%s, %s, %s, %s)", 
        #                    (name, price, quantity, category_id))

        # Insert fake orders
        # cursor.execute("SELECT id FROM user")
        # user_ids = [row[0] for row in cursor.fetchall()]
        
        # cursor.execute("SELECT id FROM product")
        # product_ids = [row[0] for row in cursor.fetchall()]
        # for _ in range(50):
        #     date = fake.date_this_year()
        #     user_id = random.choice(user_ids)
        #     cursor.execute("INSERT INTO `order` (date, user_id) VALUES (%s, %s)", 
        #                    (date, user_id))
        #     order_id = cursor.lastrowid
        #     total_price = 0 
        #     for _ in range(random.randint(1, 5)):
        #         product_id = random.choice(product_ids)
        #         quantity = random.randint(1, 10)
        #         cursor.execute("SELECT price FROM product WHERE id = %s", (product_id,))
        #         product_price = cursor.fetchone()[0]
        #         total_price += quantity * product_price
        #         cursor.execute("INSERT INTO order_item (quantity, product_id, order_id) VALUES (%s, %s, %s)", 
        #                        (quantity, product_id, order_id))
        #     cursor.execute("UPDATE `order` SET total_price = %s WHERE id = %s", (total_price, order_id))

        connection.commit()
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()
        close_connection(connection)

if __name__ == "__main__":
    create_fake_data()
