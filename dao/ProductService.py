from util.DBConnection import DBConnection
from exception.AuthenticationException import AuthenticationException
from exception.InvaliDataException import InvalidDataException
from entity.Product import Product


class ProductService(DBConnection):
    def __init__(self):
        super().__init__()

    def add_product(self):
        try:
            product = Product()
            self.open()
            product.set_product_name(input("Enter Product Name: "))
            product.set_desc(input("Enter Description: "))
            product.set_price(float(input("Enter Price: ")))
            if product.get_price() < 0:
                raise InvalidDataException("Enter Price value greater than zero...")
            query = "INSERT INTO Products (ProductName, P_Desc, Price) VALUES (%s, %s, %s);"
            self.stmt.execute(query, (product.get_product_name(), product.get_desc(), product.get_price()))
            self.conn.commit()
            print("Product added successfully...")
            self.close()
        except InvalidDataException as e:
            print(f"Product Insertion Failed: {e}")
        except Exception as e:
            print(f"Error adding product: {e}")

    def update_product(self):
        try:
            product = Product()
            self.open()
            product_id = int(input("Enter Product Id to update: "))
            query = f"SELECT * FROM Products WHERE ProductID = {product_id};"
            self.stmt.execute(query)
            product_details = self.stmt.fetchone()
            if product_details:
                try:
                    query = "UPDATE Products SET ProductName = %s, P_Desc = %s, Price = %s WHERE ProductID = %s"
                    self.stmt.execute(query,
                                      (product.get_product_name(), product.get_desc(), product.get_price(), product_id))
                    self.conn.commit()
                    print("Product updated successfully...")
                    self.close()
                except Exception as e:
                    print(f"Error updating product: {e}")
            else:
                raise InvalidDataException("ProductID not found in Database...")
        except InvalidDataException as e:
            print(f"Updation Failed: {e}")

    def remove_product(self):
        try:
            self.open()
            product_id = int(input("Enter Product Id to update: "))
            product_str = f'SELECT * FROM Products WHERE ProductID={product_id};'
            self.stmt.execute(product_str)
            records = self.stmt.fetchall()
            if records:
                query = f"DELETE FROM Products WHERE ProductID = {product_id};"
                self.stmt.execute(query)
                self.conn.commit()
                print("Product removed successfully...")
                self.close()
            else:
                raise InvalidDataException("ProductID not found in Database...")
        except InvalidDataException as e:
            print(f"Error removing product: {e}")
        except Exception as e:
            print(f"Error removing product: {e}")

    def get_all_products(self):
        try:
            self.open()
            query = "SELECT * FROM Products;"
            self.stmt.execute(query)
            products = self.stmt.fetchall()
            self.close()
            for product in products:
                print(f"ProductID: {product[0]}, ProductName: {product[1]}, P_Desc: {product[2]}, Price: {product[3]}")
        except Exception as e:
            print(f"Error retrieving products: {e}")

    def get_product_details(self):
        try:
            product_id = int(input("Enter Product Id to get details: "))
            self.open()
            query = f"SELECT * FROM Products WHERE ProductID = {product_id};"
            self.stmt.execute(query)
            product_details = self.stmt.fetchall()
            self.close()
            if product_details:
                for product in product_details:
                    print(f"ProductID: {product[0]}, ProductName: {product[1]}, P_Desc: {product[2]}, Price: {product[3]}")
            else:
                raise AuthenticationException("Product ID not found in Database...")
        except AuthenticationException as e:
            print(f'Invalid Input: {e}')

    def update_product_info(self):
        try:
            self.open()
            product_id = int(input("Enter Product Id to Update: "))
            product_str = f'SELECT * FROM Products WHERE ProductID={product_id};'
            self.stmt.execute(product_str)
            records = self.stmt.fetchall()
            if records:
                price = int(input("Enter Price: "))
                description = input("Enter Description of Product: ")
                query = f"SELECT * FROM Products WHERE ProductID = {product_id};"
                self.stmt.execute(query)
                product_details = self.stmt.fetchone()
                if product_details:
                    if price is not None:
                        query = f"UPDATE Products SET Price = {price} WHERE ProductID = {product_id};"
                        self.stmt.execute(query)
                    if description:
                        query = "UPDATE Products SET P_Desc = %s WHERE ProductID = %s"
                        self.stmt.execute(query, (description, product_id))
                    self.conn.commit()
                    print("Product information updated successfully.")
                else:
                    raise AuthenticationException("Product ID not found in Database...")
                self.close()
            else:
                raise AuthenticationException("ProductID not found in Database...")
        except AuthenticationException as e:
            print(f'Invalid Input: {e}')
        except Exception as f:
            print(f'Error Occurred: {f}')

    def is_product_in_stock(self):
        try:
            self.open()
            product_id = int(input("Enter Product Id to Check: "))
            product_str = f'SELECT * FROM Products WHERE ProductID={product_id};'
            self.stmt.execute(product_str)
            records = self.stmt.fetchall()
            if records:
                query = f"SELECT QuantityInStock FROM Inventory WHERE ProductID = {product_id};"
                self.stmt.execute(query)
                quantity = self.stmt.fetchone()[0]
                if quantity > 0:
                    print('Product is in Stock...')
                else:
                    print('Product is not in stock!!!')
                self.close()
            else:
                raise InvalidDataException("ProductID not found in Database...")
        except InvalidDataException as e:
            print(f'Error checking product stock: {e}')
        except Exception as e:
            print(f"Error checking product stock: {e}")
