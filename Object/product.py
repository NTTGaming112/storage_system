from db import create_connection, close_connection

class Product:
    """Class representing a product in the database.

    Attributes:
        id (int): The unique identifier of the product.
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The quantity of the product available in stock.
        category_id (int): The category ID of the product.
    """

    def __init__(self, id, name, price=0.0, quantity=0, category_id=None):
        """Initialize a Product instance with id, name, price, quantity, and category_id."""
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category_id = category_id

    def __str__(self):
        """Return a string representation of the product."""
        return [self.id, self.name, f"{self.price}$", self.quantity]

    @staticmethod
    def fetch(category):
        """Fetch all products in a specific category from the database.

        Args:
            category (str): The name of the category.

        Returns:
            list: A list of product details.
        """
        connection = create_connection()
        if connection is None:
            return []

        cursor = connection.cursor()
        cursor.execute("SELECT id, name, price, quantity FROM product WHERE category_id IN (SELECT id FROM category WHERE name = %s)", (category,))
        rows = cursor.fetchall()
        products = [Product(*row).__str__() for row in rows]

        cursor.close()
        close_connection(connection)
        return products
    
    @staticmethod
    def fetch_product(product_name):
        """Fetch details of a specific product from the database.

        Args:
            product_name (str): The name of the product.

        Returns:
            tuple: A tuple containing product details.
        """
        connection = create_connection()
        if connection is None:
            return []

        cursor = connection.cursor()
        cursor.execute("SELECT id, price, quantity FROM product WHERE name = %s" , (product_name,))
        product = cursor.fetchone()
        cursor.close()
        close_connection(connection)
        return product

    @staticmethod
    def add(product_data, category_name):
        """Add a new product to the database.

        Args:
            product_data (dict): A dictionary containing product data.
            category_name (str): The name of the category to which the product belongs.

        Returns:
            bool: True if the product is successfully added, False otherwise.
        """
        connection = create_connection()
        if connection is None:
            return False

        cursor = connection.cursor()
        cursor.execute("SELECT id FROM category WHERE name = %s", (category_name,))
        category_id = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM product WHERE name = %s AND category_id = %s", (product_data['name'],category_id))

        if cursor.fetchone()[0] > 0:
            cursor.close()
            close_connection(connection)
            return False

        cursor.execute("""
            INSERT INTO product (name, price, quantity, category_id) 
            VALUES (%s, %s, %s, %s)
        """, (product_data['name'], product_data['price'], product_data['quantity'], category_id))
        connection.commit()
        cursor.close()
        close_connection(connection)
        return True

    @staticmethod
    def update(product_id, column, value, category_name):
        """Update product information in the database.

        Args:
            product_id (int): The ID of the product to be updated.
            column (str): The column name to be updated.
            value (str): The new value of the column.
            category_name (str): The name of the category to which the product belongs.

        Returns:
            bool: True if the product information is successfully updated, False otherwise.
        """
        connection = create_connection()
        if connection is None:
            return False

        try:
            cursor = connection.cursor()
            cursor.execute("SELECT id FROM category WHERE name = %s", (category_name,))
            category_id = cursor.fetchone()[0]
            if column == 'name':
                cursor.execute("SELECT COUNT(*) FROM product WHERE name = %s AND id != %s AND category_id = %s", (value, product_id, category_id))
                if cursor.fetchone()[0] > 0:
                    cursor.close()
                    close_connection(connection)
                    return False

            query = f"UPDATE product SET {column} = %s WHERE id = %s"
            cursor.execute(query, (value, product_id))
            connection.commit()
            return True
        
        except Exception as e:
            print(f"Error updating product: {e}")
            return False
        finally:
            cursor.close()
            close_connection(connection)

    @staticmethod
    def update_quantity(product_id, sell):
        """Update the quantity of a product in the database after a sale.

        Args:
            product_id (int): The ID of the product.
            sell (int): The quantity sold.

        Returns:
            bool: True if the quantity is successfully updated, False otherwise.
        """
        connection = create_connection()
        if connection is None:
            return False
        
        cursor = connection.cursor()
        cursor.execute("SELECT quantity FROM product WHERE id = %s", (product_id,))
        quantity = cursor.fetchone()[0]
        new_quantity = quantity - sell
        cursor.execute("UPDATE product SET quantity = %s WHERE id = %s", (new_quantity, product_id))
        connection.commit()

        cursor.close()
        close_connection(connection)
        return True

    @staticmethod
    def delete(product_id, category_name):
        """Delete a product from the database.

        Args:
            product_id (int): The ID of the product to be deleted.
            category_name (str): The name of the category to which the product belongs.

        Returns:
            bool: True if the product is successfully deleted, False otherwise.
        """
        connection = create_connection()
        if connection is None:
            return False

        cursor = connection.cursor()
        cursor.execute("SELECT id FROM category WHERE name = %s", (category_name,))
        category_id = cursor.fetchone()[0]
        cursor.execute("DELETE FROM order_item WHERE product_id = %s", (product_id,))
        cursor.execute("DELETE FROM `order` WHERE id IN (SELECT order_id FROM order_item WHERE product_id = %s)", (product_id,))
        cursor.execute("DELETE FROM product WHERE id = %s AND category_id = %s", (product_id, category_id))
        connection.commit()

        cursor.close()
        close_connection(connection)
        return True
