from db import *

class User:
    """
    A class to represent a user in the database.
    
    Attributes:
    -----------
    id : int
        Unique identifier for the user.
    username : str
        Username of the user.
    password : str
        Password of the user.
    address : str
        Address of the user.
    phone : str
        Phone number of the user.
    email : str
        Email of the user.
    data : list
        List of attributes for the user.
    """

    def __init__(self, id, username, password, address, phone, email):
        """
        Constructs all the necessary attributes for the user object.

        Parameters:
        -----------
        id : int
            Unique identifier for the user.
        username : str
            Username of the user.
        password : str
            Password of the user.
        address : str
            Address of the user.
        phone : str
            Phone number of the user.
        email : str
            Email of the user.
        """
        self.id = id
        self.username = username
        self.password = password
        self.address = address
        self.phone = phone
        self.email = email
        self.data = ["username", "password", "address", "phone", "email"]

    def __str__(self):
        """
        Returns a string representation of the user object.

        Returns:
        --------
        str
            String representation of the user.
        """
        return [self.id, self.username, self.password, self.address, self.phone, self.email]

    @staticmethod
    def fetch():
        """
        Fetches all users from the database.

        Returns:
        --------
        list
            A list of user objects.
        """
        connection = create_connection()
        if connection is None:
            return []

        cursor = connection.cursor()
        cursor.execute("SELECT id, username, password, address, phone, email FROM user")
        rows = cursor.fetchall()
        users = [User(*row).__str__() for row in rows]

        cursor.close()
        close_connection(connection)
        return users
    
    @staticmethod
    def fetch_id(username):
        """
        Fetches the user ID for a given username.

        Parameters:
        -----------
        username : str
            Username of the user.

        Returns:
        --------
        int
            User ID corresponding to the username.
        """
        connection = create_connection()
        if connection is None:
            return None

        cursor = connection.cursor()
        cursor.execute("SELECT id FROM user WHERE username = %s", (username,))
        user_id = cursor.fetchone()[0]
        
        cursor.close()
        close_connection(connection)
        return user_id

    @staticmethod
    def add(user_data):
        """
        Adds a new user to the database.

        Parameters:
        -----------
        user_data : dict
            Dictionary containing user information.

        Returns:
        --------
        bool
            True if user is added successfully, False otherwise.
        """
        connection = create_connection()
        if connection is None:
            return False

        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM user WHERE username = %s", (user_data['username'],))
        if cursor.fetchone()[0] > 0:
            cursor.close()
            close_connection(connection)
            return False

        cursor.execute("""
            INSERT INTO user (username, password, address, phone, email) 
            VALUES (%s, %s, %s, %s, %s)
        """, (user_data['username'], user_data['password'], user_data['address'], user_data['phone'], user_data['email']))
        connection.commit()
        cursor.close()
        close_connection(connection)
        return True

    @staticmethod
    def update(user_id, column, value):
        """
        Updates user information in the database.

        Parameters:
        -----------
        user_id : int
            Unique identifier for the user.
        column : str
            Column to be updated.
        value : str
            New value for the column.

        Returns:
        --------
        bool
            True if user is updated successfully, False otherwise.
        """
        connection = create_connection()
        if connection is None:
            return False

        try:
            cursor = connection.cursor()
            if column == 'username':
                cursor.execute("SELECT COUNT(*) FROM user WHERE username = %s AND id != %s", (value, user_id))
                if cursor.fetchone()[0] > 0:
                    
                    cursor.close()
                    close_connection(connection)
                    return False

            query = f"UPDATE user SET {column} = %s WHERE id = %s"
            cursor.execute(query, (value, user_id))
            connection.commit()
            return True
        
        except Exception as e:
            print(f"Error updating user: {e}")
            return False
        finally:
            cursor.close()
            close_connection(connection)

    @staticmethod
    def delete(user_id):
        """
        Deletes a user from the database.

        Parameters:
        -----------
        user_id : int
            Unique identifier for the user.

        Returns:
        --------
        bool
            True if user is deleted successfully, False otherwise.
        """
        connection = create_connection()
        if connection is None:
            return False

        cursor = connection.cursor()
        cursor.execute("DELETE FROM order_item WHERE order_id IN (SELECT id FROM `order` WHERE user_id = %s)", (user_id,))
        cursor.execute("DELETE FROM `order` WHERE user_id = %s", (user_id,))
        cursor.execute("DELETE FROM user WHERE id = %s", (user_id,))
        connection.commit()

        cursor.close()
        close_connection(connection)
        return True
