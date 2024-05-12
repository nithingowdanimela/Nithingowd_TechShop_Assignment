import mysql.connector as sql
from exception.DatabaseConnectionException import DatabaseConnectionException


class DBConnection:

    def __init__(self, host='localhost', database='TechShop', user='root', password='Nithin@2003'):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conn = None
        self.stmt = None

    def open(self):
        try:
            self.conn = sql.connect(host='localhost', database='TechShop', user='root', password='Nithin@2003')
            # connecting with database
            if self.conn.is_connected():
                print("Database Is Connected....")
                self.conn.commit()
            else:
                raise DatabaseConnectionException("Not Connected with Database....")
            self.stmt = self.conn.cursor()
        except DatabaseConnectionException as e:
            print(f'Database Connection Error: {e}')

    def close(self):
        self.conn.close()
        print("Database Connection is Closed...")


obj = DBConnection()
obj.open()
obj.close()
