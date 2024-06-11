from db import create_connection, close_connection

class Order:
    """Class representing an order in the database.

    Attributes:
        id (int): The unique identifier of the order.
        date (datetime): The date and time when the order was placed.
        total_price (float): The total price of the order.
        user_id (int): The ID of the user who placed the order.
    """

    def __init__(self, id, date, total_price=0.0, user_id=None):
        """Initialize an Order instance with id, date, total_price, and user_id."""
        self.id = id
        self.date = date
        self.total_price = total_price
        self.user_id = user_id

    def __str__(self):
        """Return a string representation of the order."""
        return [self.id, self.date, f"{self.total_price}$"]

    @staticmethod
    def fetch(name_id):
        """Fetch all orders placed by a specific user from the database.

        Args:
            name_id (str): The username of the user.

        Returns:
            list: A list of order details.
        """
        connection = create_connection()
        if connection is None:
            return []

        cursor = connection.cursor()
        cursor.execute("SELECT id, date, total_price, user_id FROM `order` WHERE user_id IN (SELECT id FROM user WHERE username = %s)", (name_id,))
        rows = cursor.fetchall()
        orders = [Order(*row).__str__() for row in rows]

        cursor.close()
        close_connection(connection)
        return orders 
    
    @staticmethod
    def add(date, total_price, user_id):
        """Add a new order to the database.

        Args:
            date (datetime): The date and time when the order was placed.
            total_price (float): The total price of the order.
            user_id (int): The ID of the user who placed the order.

        Returns:
            int: The ID of the newly added order if successful, False otherwise.
        """
        connection = create_connection()
        if connection is None:
            return False
        
        cursor = connection.cursor()
        cursor.execute("INSERT INTO `order` (date, total_price, user_id) VALUES (%s, %s, %s)", (date, total_price, user_id))
        order_id = cursor.lastrowid
        connection.commit()
        cursor.close()
        close_connection(connection)
        return order_id

    @staticmethod
    def delete(order_id):
        """Delete an order from the database.

        Args:
            order_id (int): The ID of the order to be deleted.

        Returns:
            bool: True if the order is successfully deleted, False otherwise.
        """
        connection = create_connection()
        if connection is None:
            return False

        cursor = connection.cursor()
        cursor.execute("DELETE FROM order_item WHERE order_id = %s", (order_id,))      
        cursor.execute("DELETE FROM `order` WHERE id = %s", (order_id,))
        connection.commit()

        cursor.close()
        close_connection(connection)
        return True
