from util.DBConnection import DBConnection
from exception.AuthenticationException import AuthenticationException
from exception.InsufficientStockException import InsufficientStockException
from entity.Inventory import Inventory


class InventoryService(DBConnection):
    def __init__(self):
        super().__init__()

    def add_inventory(self):
        try:
            inventory = Inventory()
            self.open()
            inventory.set_product(int(input("Enter ProductID: ")))
            inventory.set_quantity_in_stock(int(input("Enter Quantity in stock: ")))
            inventory.set_last_stock_update(input("Enter Last Stock updated Date: "))
            query = "INSERT INTO Inventory (ProductID, QuantityInStock, LastStockUpdate) VALUES (%s, %s, %s)"
            self.stmt.execute(query, (
                inventory.get_product(), inventory.get_quantity_in_stock(), inventory.get_last_stock_update()))
            self.conn.commit()
            print("Inventory added successfully...")
            self.close()
        except Exception as e:
            print(f"Error adding inventory: {e}")

    def update_inventory(self):
        try:
            inventory = Inventory()
            self.open()
            inventory_id = int(input("Enter InventoryID: "))
            inventory.set_product(int(input("Enter ProductID: ")))
            inventory.set_quantity_in_stock(int(input("Enter Quantity in stock: ")))
            query = "UPDATE Inventory SET ProductID = %s, QuantityInStock = %s, LastStockUpdate = CURDATE() WHERE InventoryID = %s;"
            self.stmt.execute(query, (inventory.get_product(), inventory.get_quantity_in_stock(), inventory_id))
            self.conn.commit()
            print("Inventory updated successfully...")
            self.close()
        except Exception as e:
            print(f"Error updating inventory: {e}")

    def remove_inventory(self):
        try:
            self.open()
            inventory_id = int(input("Enter InventoryID: "))
            query = f"DELETE FROM Inventory WHERE InventoryID = {inventory_id};"
            self.stmt.execute(query)
            self.conn.commit()
            print("Inventory removed successfully...")
            self.close()
        except Exception as e:
            print(f"Error removing inventory: {e}")

    def get_all_inventory(self):
        try:
            self.open()
            query = "SELECT * FROM Inventory;"
            self.stmt.execute(query)
            inventory = self.stmt.fetchall()
            self.close()
            for i in inventory:
                print(i)
        except Exception as e:
            print(f"Error retrieving inventory: {e}")

    def get_product(self):
        try:
            self.open()
            product_id = int(input("Enter ProductID: "))
            query = f"SELECT * FROM Inventory WHERE ProductID = {product_id};"
            self.stmt.execute(query)
            result = self.stmt.fetchone()
            if result:
                print(result)
                self.close()
            else:
                raise AuthenticationException("ProductID not found in Database...")
        except AuthenticationException as e:
            print(f"Error retrieving product details: {e}")

    def get_quantity_in_stock(self):
        try:
            self.open()
            product_id = int(input("Enter ProductID to get Stock: "))
            query = f"SELECT QuantityInStock FROM Inventory JOIN Products ON Inventory.ProductId=Products.ProductID WHERE Inventory.ProductID = {product_id};"
            self.stmt.execute(query)
            result = self.stmt.fetchone()
            if result:
                print(f'Quantity in stock for Product {product_id}: {result[0]};')
                self.close()
            else:
                raise AuthenticationException("ProductID not found in Database...")
        except AuthenticationException as e:
            print(f"Error retrieving product details: {e}")

    def get_quantity(self, product_id):
        try:
            self.open()
            query = f"SELECT QuantityInStock FROM Inventory WHERE ProductID = {product_id};"
            self.stmt.execute(query)
            result = self.stmt.fetchone()[0]
            if result:
                return result
                #print(f'Quantity of ProductID {product_id}: {result}')
                #self.close()
            else:
                raise AuthenticationException("ProductID not found in Database...")
        except AuthenticationException as e:
            print(f"Error retrieving product details: {e}")

    def add_to_inventory(self):
        try:
            self.open()
            product_id = int(input("Enter ProductID to add Stock: "))
            quantity = int(input("Enter No of quantities to be added: "))
            current_quantity = self.get_quantity(product_id)
            query = f"SELECT * FROM Inventory WHERE ProductID = {product_id}"
            self.stmt.execute(query)
            result = self.stmt.fetchall()
            if result:
                try:
                    new_quantity = current_quantity + quantity
                    query = f"UPDATE Inventory SET QuantityInStock={new_quantity} WHERE ProductID = {product_id};"
                    self.stmt.execute(query)
                    self.conn.commit()
                    print("Stock Added Successfully...")
                    self.close()
                except Exception as e:
                    print(f'Error in Updating Inventory: {e}')
            else:
                raise AuthenticationException("ProductID not found in Database...")
        except AuthenticationException as e:
            print(f"Error retrieving product details: {e}")

    def remove_from_inventory(self):
        try:
            self.open()
            product_id = int(input("Enter ProductID to get Stock: "))
            quantity = int(input("Enter No of quantities to be removed: "))
            current_quantity = self.get_quantity(product_id)
            query = f"SELECT * FROM Inventory WHERE ProductID = {product_id};"
            self.stmt.execute(query)
            result = self.stmt.fetchone()
            if result:
                try:
                    if current_quantity - quantity >= 0:
                        new_quantity = current_quantity - quantity
                        query = f"UPDATE Inventory SET QuantityInStock={new_quantity} WHERE ProductID = {product_id};"
                        self.stmt.execute(query)
                        self.conn.commit()
                        print("Stock Removed successfully...")
                        self.close()
                    else:
                        raise InsufficientStockException(f"Cannot remove more items than available in stock.")
                except InsufficientStockException as e:
                    print(f'Error in Removing Inventory: {e}')
            else:
                raise AuthenticationException("ProductID not found in Database...")
        except AuthenticationException as e:
            print(f"Error retrieving product details: {e}")
        except Exception as e:
            print(f'Error Occurred: {e}')

    def update_stock_quantity(self):
        try:
            self.open()
            product_id = int(input("Enter ProductID to get Stock: "))
            quantity = int(input("Enter New Quantity to be added: "))
            query = f"SELECT * FROM Inventory WHERE ProductID = {product_id};"
            self.stmt.execute(query)
            result = self.stmt.fetchall()
            if result:
                try:
                    query = f"UPDATE Inventory SET QuantityInStock={quantity} WHERE ProductID = {product_id};"
                    self.stmt.execute(query)
                    self.conn.commit()
                    print("Stock Updated Successfully...")
                    self.close()
                except Exception as e:
                    print(f'Error in Updating Inventory: {e}')
            else:
                raise AuthenticationException("ProductID not found in Database...")
        except AuthenticationException as e:
            print(f"Error retrieving product details: {e}")

    def is_product_available(self):
        try:
            product_id = int(input("Enter ProductID to get Stock: "))
            quantity = int(input("Enter No of quantities to be checked: "))
            current_quantity = self.get_quantity(product_id)
            if quantity <= current_quantity:
                print(f"ProductID: {product_id} is available...")
            else:
                print(f"ProductID: {product_id} is not available...")
        except Exception as e:
            print(f"Error retrieving product availability: {e}")

    def get_inventory_value(self):
        try:
            self.open()
            query = "SELECT SUM(p.Price * i.QuantityInStock) FROM Inventory i JOIN Products p ON i.ProductID = p.ProductID;"
            self.stmt.execute(query)
            total_value = self.stmt.fetchone()[0]
            if total_value > 0:
                print(f"Total Value of Products in Inventory : {total_value}")
        except Exception as e:
            print(f"Error calculating total inventory value: {e}")

    def list_low_stock_products(self):
        try:
            self.open()
            threshold = int(input("Enter Threshold to be checked: "))
            query = f"SELECT i.*, p.ProductName FROM Inventory i JOIN Products p ON i.ProductID = p.ProductID WHERE i.QuantityInStock < {threshold};"
            self.stmt.execute(query)
            low_stock_products = self.stmt.fetchall()
            for product in low_stock_products:
                print(f"Product ID: {product[1]}, Product Name: {product[4]}, Quantity in stock: {product[2]}")
            self.close()
        except Exception as e:
            print(f"Error listing low stock products: {e}")

    def list_out_of_stock_products(self):
        try:
            self.open()
            query = "SELECT i.*, p.ProductName FROM Inventory i JOIN Products p ON i.ProductID = p.ProductID WHERE i.QuantityInStock = 0;"
            self.stmt.execute(query)
            out_of_stock_products = self.stmt.fetchall()
            for product in out_of_stock_products:
                print(f"Product ID: {product[1]}, Product Name: {product[5]}, Quantity in stock: {product[3]}")
            self.close()
        except Exception as e:
            print(f"Error listing out of stock products: {e}")

    def list_all_products(self):
        try:
            self.open()
            query = "SELECT i.*, p.ProductName FROM Inventory i JOIN Products p ON i.ProductID = p.ProductID;"
            self.stmt.execute(query)
            all_products = self.stmt.fetchall()
            for product in all_products:
                print(f"Product ID: {product[1]}, Product Name: {product[4]}, Quantity in stock: {product[2]}")
            self.close()
        except Exception as e:
            print(f"Error listing all products: {e}")
