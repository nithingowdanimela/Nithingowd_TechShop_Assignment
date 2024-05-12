from exception.AuthenticationException import AuthenticationException
from exception.IncompleteOrderException import IncompleteOrderException
from util.DBConnection import DBConnection
from entity.Order import Order


class OrderService(DBConnection):
    def __init__(self):
        super().__init__()

    def add_order(self):
        try:
            order = Order()
            self.open()
            order.set_customer_id(int(input("Enter Customer ID: ")))
            order.set_order_date(input("Enter Order Date: "))
            order.set_total_amount(input("Enter Total Amount: "))
            query = "INSERT INTO Orders (CustomerID, OrderDate, TotalAmount) VALUES (%s, %s, %s);"
            self.stmt.execute(query, (order.get_customer_id(), order.get_order_date(), order.get_total_amount()))
            self.conn.commit()
            print("Order added successfully...")
            self.close()
        except Exception as e:
            print(f"Error adding order: {e}")

    def remove_order(self):
        try:
            self.open()
            order_id = int(input("Enter OrderID to delete: "))
            query = f"DELETE FROM Orders WHERE OrderID = {order_id};"
            self.stmt.execute(query)
            self.conn.commit()
            print("Order removed successfully...")
            self.close()
        except Exception as e:
            print(f"Error removing order: {e}")

    def get_all_orders(self):
        try:
            self.open()
            query = "SELECT * FROM Orders;"
            self.stmt.execute(query)
            orders = self.stmt.fetchall()
            for i in orders:
                print(f"OrderID: {i[0]}, CustomerID: {i[1]}, OrderDate: {i[2]}, Total Amount: {i[3]}")
            self.close()
        except Exception as e:
            print(f"Error retrieving orders: {e}")

    def calculate_total_amount(self):
        try:
            order_id = int(input("Enter OrderId to get details: "))
            self.open()
            cus_str = f'SELECT * FROM Orders WHERE OrderID={order_id};'
            self.stmt.execute(cus_str)
            records = self.stmt.fetchall()
            self.conn.commit()
            if records:
                query = (f'''
                SELECT SUM(Quantity * Price) FROM OrderDetails INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID WHERE OrderID = {order_id};s
                ''')
                self.stmt.execute(query)
                total_amount = self.stmt.fetchone()[0]
                print(f'Total Amount for OrderID {order_id} : {total_amount}')
                self.close()
            else:
                raise AuthenticationException("OrderID not found in Database...")
        except AuthenticationException as e:
            print(f'Authentication Error: {e}')

    def get_order_details(self):
        try:
            order_id = int(input("Enter OrderId to get details: "))
            self.open()
            ord_str = f'SELECT * FROM Orders WHERE OrderId={order_id};'
            self.stmt.execute(ord_str)
            records = self.stmt.fetchall()
            self.conn.commit()
            if records:
                print()
                print("...............Order Details for orderID: ", order_id, "...............")
                for i in records:
                    print(f"OrderID: {i[0]}, CustomerID: {i[1]}, OrderDate: {i[2]}, TotalAmount: {i[3]}")
                print()
                self.close()
            else:
                raise IncompleteOrderException("OrderID not found in Database...")
        except IncompleteOrderException as e:
            print(f"Invalid Input : {e}")

    def update_order_status(self):
        try:
            order_id = int(input("Enter OrderId to get details: "))
            self.open()
            ord_str = f'SELECT * FROM Orders WHERE OrderId={order_id};'
            self.stmt.execute(ord_str)
            records = self.stmt.fetchall()
            self.conn.commit()
            if records:
                status = input("Enter Status of Order: ")
                query = f"UPDATE Orders SET OrderStatus = {status} WHERE OrderID = {order_id};"
                self.stmt.execute(query)
                self.conn.commit()
                self.close()
            else:
                raise IncompleteOrderException("OrderID not found in Database...")
        except IncompleteOrderException as e:
            print(f"Updation Failed : {e}")

    def cancel_order(self):
        try:
            order_id = int(input("Enter OrderId to get details: "))
            self.open()
            ord_str = f'SELECT * FROM Orders WHERE OrderId={order_id};'
            self.stmt.execute(ord_str)
            records = self.stmt.fetchall()
            if records:
                query = f"DELETE FROM OrderDetails WHERE OrderID = {order_id};"
                self.stmt.execute(query)
                self.conn.commit()
                query = f"UPDATE Orders SET OrderStatus = 'Cancelled' WHERE OrderID = {order_id};"
                self.stmt.execute(query)
                self.conn.commit()
                self.close()
            else:
                raise IncompleteOrderException("OrderID not found in Database...")
        except IncompleteOrderException as e:
            print(f"Cancellation Failed : {e}")
