from db import create_connection, close_connection

class OrderItem:
    """Class representing an item in an order in the database.

    Attributes:
        id (int): The unique identifier of the order item.
        quantity (int): The quantity of the product in the order item.
        product_id (int): The ID of the product associated with the order item.
        order_id (int): The ID of the order associated with the order item.
    """

    def __init__(self, id, quantity, product_id=None, order_id=None):
        """Initialize an OrderItem instance with id, quantity, product_id, and order_id."""
        self.id = id
        self.quantity = quantity
        self.product_id = product_id
        self.order_id = order_id

    def __str__(self):
        """Return a string representation of the order item."""
        connection = create_connection()
        if connection is None:
            return []

        cursor = connection.cursor()
        cursor.execute("SELECT name, price FROM product WHERE id = %s", (self.product_id,))
        product = cursor.fetchone()        
        return [product[0], f"{product[1]}$", self.quantity, f"{product[1]*self.quantity}$"]

    @staticmethod
    def fetch(order):
        """Fetch all order items associated with a specific order from the database.

        Args:
            order (int): The ID of the order.

        Returns:
            list: A list of order item details.
        """
        connection = create_connection()
        if connection is None:
            return []

        cursor = connection.cursor()

        cursor.execute("SELECT id, quantity, product_id FROM order_item WHERE order_id IN (SELECT id FROM `order` WHERE id = %s)", (order,))
        rows = cursor.fetchall()
        order_items = [OrderItem(*row).__str__() for row in rows]

        cursor.close()
        close_connection(connection)
        return order_items

    @staticmethod
    def add(quantity, product_id, order_id):
        """Add a new order item to the database.

        Args:
            quantity (int): The quantity of the product in the order item.
            product_id (int): The ID of the product associated with the order item.
            order_id (int): The ID of the order associated with the order item.

        Returns:
            bool: True if the order item is successfully added, False otherwise.
        """
        connection = create_connection()
        if connection is None:
            return False

        cursor = connection.cursor()
        cursor.execute("INSERT INTO order_item (quantity, product_id, order_id) VALUES (%s, %s, %s)",
                    (quantity, product_id, order_id))
        connection.commit()

        cursor.close()
        close_connection(connection)
        return True
