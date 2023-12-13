import os
import mysql.connector


class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            port=3306,
            database='flight_game',
            user='obonte',
            password='Lontoo2023',
            autocommit=True
        )

    def get_conn(self):
        return self.conn
