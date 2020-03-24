import os
import mysql.connector

class DatabaseConnection:
    
    def __init__(self):
        config = {
            "user": os.getenv("MYSQL_USER"),
            "password": os.getenv("MYSQL_ROOT_PASSWORD"),
            "host": "db",
            "port": "3306",
            "database": os.getenv("MYSQL_DATABASE")
        }
        self.db_connection = mysql.connector.connect(**config)
    
    def get_cursor(self):
        return self.db_connection.cursor()
    
    def commit(self):
        self.db_connection.commit()
    
    def close_connection(self):
        self.db_connection.close()

    def close_Cursor(self):
        self.get_cursor().close()
