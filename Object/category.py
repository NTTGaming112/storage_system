from db import create_connection

class Category:
    """Class representing a category in the database.

    Attributes:
        id (int): The unique identifier of the category.
        name (str): The name of the category.
    """

    def __init__(self, id, name):
        """Initialize a Category instance with id and name."""
        self.id = id
        self.name = name

    def __str__(self):
        """Return a string representation of the category."""
        return [self.name]

    @staticmethod
    def fetch():
        """Fetch all categories from the database.

        Returns:
            list: A list of category names.
        """
        connection = create_connection()
        if connection is None:
            return []

        cursor = connection.cursor()
        cursor.execute("SELECT id, name FROM category")
        rows = cursor.fetchall()
        categories = [Category(*row).__str__() for row in rows]

        cursor.close()
        connection.close()
        return categories
