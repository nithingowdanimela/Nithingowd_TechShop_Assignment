from util.DBConnection import DBConnection
from exception.AuthenticationException import AuthenticationException
from entity.OrderDetails import OrderDetails
from exception.InvaliDataException import InvalidDataException
from decimal import Decimal


class OrderDetailsService(DBConnection):
    def __init__(self):
        super().__init__()

    def add_order_detail(self):
        try:
            self.open()
            order_detail = OrderDetails()
            order_detail.set_order_id(int(input("Enter OrderID: ")))
            order_detail.set_product_id(int(input("Enter ProductID: ")))
            order_detail.set_quantity(int(input("Enter Quantity: ")))
            query = "INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES (%s, %s, %s)"
            self.stmt.execute(query,
                              (order_detail.get_order_id(), order_detail.get_product_id(), order_detail.get_quantity()))
            self.conn.commit()
            print("Order detail added successfully...")
            self.close()
        except Exception as e:
            print(f"Error adding order detail: {e}")

    def update_order_detail(self):
        try:
            self.open()
            order_detail = OrderDetails()
            order_detail_id = int(input("Enter OrderDetail ID to update: "))
            order_details_str = f'SELECT * FROM OrderDetails WHERE OrderDetailID={order_detail_id};'
            self.stmt.execute(order_details_str)
            records = self.stmt.fetchall()
            self.conn.commit()
            if records:
                order_detail.set_order_id(int(input("Enter OrderID: ")))
                order_detail.set_product_id(int(input("Enter ProductID: ")))
                order_detail.set_quantity(int(input("Enter Quantity: ")))
                query = "UPDATE OrderDetails SET OrderID = %s, ProductID = %s, Quantity = %s WHERE OrderDetailID = %s"
                self.stmt.execute(query, (
                    order_detail.get_order_id(), order_detail.get_product_id(), order_detail.get_quantity(), order_detail_id))
                self.conn.commit()
                print("Order detail updated successfully...")
                self.close()
            else:
                raise InvalidDataException("OrderDetails ID not found in Database...")
        except InvalidDataException as e:
            print(f"Error updating order detail: {e}")
        except Exception as e:
            print(f"Error updating order detail: {e}")

    def remove_order_detail(self):
        try:
            self.open()
            order_detail_id = int(input("Enter OrderDetail ID: "))
            order_details_str = f'SELECT * FROM OrderDetails WHERE OrderDetailID={order_detail_id};'
            self.stmt.execute(order_details_str)
            records = self.stmt.fetchall()
            self.conn.commit()
            if records:
                query = f"DELETE FROM OrderDetails WHERE OrderDetailID ={order_detail_id};"
                self.stmt.execute(query)
                self.conn.commit()
                print("Order detail removed successfully...")
                self.close()
            else:
                raise InvalidDataException("OrderDetails ID not found in Database...")
        except InvalidDataException as e:
            print(f"Error Removing order details: {e}")
        except Exception as e:
            print(f"Error removing order details: {e}")

    def get_all_order_details(self):
        try:
            self.open()
            query = "SELECT * FROM OrderDetails;"
            self.stmt.execute(query)
            order_details = self.stmt.fetchall()
            self.close()
            return order_details
        except Exception as e:
            print(f"Error retrieving order details: {e}")

    def calculate_subtotal(self):
        try:
            order_detail_id = int(input("Enter OrderDetail Id to calculate Subtotal: "))
            self.open()
            cus_str = f'SELECT * FROM OrderDetails WHERE OrderDetailID={order_detail_id};'
            self.stmt.execute(cus_str)
            records = self.stmt.fetchall()
            self.conn.commit()
            if records:
                try:
                    query = f"SELECT Price, Quantity FROM OrderDetails INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID WHERE OrderDetailID = {order_detail_id}"
                    self.stmt.execute(query)
                    result = self.stmt.fetchone()
                    subtotal = result[0] * result[1] if result else None
                    print(f'Sub Total for OrderDetail ID {order_detail_id}: {subtotal}')
                    self.close()
                except Exception as e:
                    print(f"Error calculating subtotal: {e}")
            else:
                raise AuthenticationException("OrderDetail ID not found in Database...")
        except AuthenticationException as e:
            print(f'Invalid Input: {e}')

    def calculate_total(self, order_detail_id):
        try:
            self.open()
            cus_str = f'SELECT * FROM OrderDetails WHERE OrderDetailID={order_detail_id};'
            self.stmt.execute(cus_str)
            records = self.stmt.fetchall()
            self.conn.commit()
            if records:
                try:
                    query = f"SELECT Price, Quantity FROM OrderDetails INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID WHERE OrderDetailID = {order_detail_id}"
                    self.stmt.execute(query)
                    result = self.stmt.fetchone()
                    subtotal = result[0] * result[1] if result else None
                    self.close()
                    return subtotal
                except Exception as e:
                    print(f"Error calculating subtotal: {e}")
            else:
                raise AuthenticationException("OrderDetail ID not found in Database...")
        except AuthenticationException as e:
            print(f'Invalid Input: {e}')

    def get_order_detail_info(self):
        try:
            order_detail_id = int(input("Enter OrderDetail Id to get details: "))
            self.open()
            cus_str = f'SELECT * FROM OrderDetails WHERE OrderDetailID={order_detail_id};'
            self.stmt.execute(cus_str)
            records = self.stmt.fetchall()
            self.conn.commit()
            if records:
                try:
                    query = f"SELECT * FROM OrderDetails WHERE OrderDetailID = {order_detail_id};"
                    self.stmt.execute(query)
                    result = self.stmt.fetchall()
                    print(f'------Order Details for ID {order_detail_id}------')
                    for i in result:
                        print(f"OrderDetailID: {i[0]}, OrderID: {i[1]}, ProductID: {i[2]}, Quantity: {i[3]}")
                    self.close()
                except Exception as e:
                    print(f"Error retrieving order detail information: {e}")
            else:
                raise AuthenticationException("OrderDetail ID not found in Database...")
        except AuthenticationException as e:
            print(f'Invalid Input: {e}')

    def update_quantity(self):
        try:
            order_detail_id = int(input("Enter OrderDetail Id to update quantity: "))
            self.open()
            cus_str = f'SELECT * FROM OrderDetails WHERE OrderDetailID={order_detail_id};'
            self.stmt.execute(cus_str)
            records = self.stmt.fetchall()
            self.conn.commit()
            if records:
                try:
                    new_quantity = int(input("Enter new quantity: "))
                    query = f"UPDATE OrderDetails SET Quantity = {new_quantity} WHERE OrderDetailID = {order_detail_id}"
                    self.stmt.execute(query)
                    self.conn.commit()
                    print("Quantity updated successfully.")
                    self.close()
                except Exception as e:
                    self.conn.rollback()
                    print(f"Error updating quantity: {e}")
            else:
                raise AuthenticationException("OrderDetail ID not found in Database...")
        except AuthenticationException as e:
            print(f'Invalid Input: {e}')

    def add_discount(self):
        try:
            order_detail_id = int(input("Enter OrderDetail Id to add Discount: "))
            self.open()
            cus_str = f'SELECT * FROM OrderDetails WHERE OrderDetailID={order_detail_id};'
            self.stmt.execute(cus_str)
            records = self.stmt.fetchall()
            if records:
                try:
                    discount = int(input("Enter Discount: "))
                    total_amount = self.calculate_total(order_detail_id)
                    if total_amount >= 0:
                        discount_amount = Decimal(total_amount) * Decimal(discount / 100)
                        discounted_total_amount = Decimal(total_amount) - discount_amount
                        query = f"UPDATE Orders SET TotalAmount ={discounted_total_amount} WHERE OrderID = (SELECT OrderID FROM OrderDetails WHERE OrderDetailID = {order_detail_id})"
                        self.stmt.execute(query)
                        self.conn.commit()
                        print("Discount applied successfully.")
                        self.close()
                    else:
                        print("Failed to apply discount. Total amount calculation failed.")
                    self.close()
                except Exception as e:
                    self.conn.rollback()
                    print(f"Error applying discount: {e}")
            else:
                raise AuthenticationException("OrderDetail ID not found in Database...")
        except AuthenticationException as e:
            print(f'Invalid Input: {e}')
