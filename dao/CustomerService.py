from util.DBConnection import DBConnection
from entity.Customer import Customer
from exception.AuthenticationException import AuthenticationException
from exception.InvaliDataException import InvalidDataException


def authenticate_phone(phone_number):
    if phone_number.isalnum() and len(phone_number) == 10:
        return True
    else:
        if len(phone_number) != 10:
            raise InvalidDataException("Enter 10 Digit PhoneNo")
        else:
            raise InvalidDataException("Enter Digits only...")


def authenticate_customer_(name):
    if name.isalpha():
        return True
    else:
        raise AuthenticationException("Enter Correct Details...")


class CustomerService(DBConnection):
    def __init__(self):
        super().__init__()

    def register_customer(self):
        customer = Customer()
        try:
            first_name = input("Enter First Name of Customer: ")
            if authenticate_customer_(first_name):
                customer.set_first_name(first_name)
        except AuthenticationException as e:
            print(f'Invalid Input: {e}')
            return
        try:
            last_name = input("Enter Last Name of Customer: ")
            if authenticate_customer_(last_name):
                customer.set_last_name(last_name)
        except InvalidDataException as e:
            print(f'Invalid Input: {e}')
            return
        customer.set_email(input("Enter Email of Customer: "))
        try:
            phone_number = input("Enter Phone Number of Customer: ")
            if authenticate_phone(phone_number):
                customer.set_phone_number(phone_number)
        except InvalidDataException as e:
            print(f'Invalid Input: {e}')
            return
        customer.set_address(input("Enter Address of Customer: "))
        data = [customer.get_first_name(), customer.get_last_name(), customer.get_email(), customer.get_phone_number(), customer.get_address()]
        insert_query = '''
        INSERT INTO Customers (FirstName, LastName, Email, Phone, Address)
        VALUES (%s, %s, %s, %s, %s);
        '''
        self.open()
        self.stmt.execute(insert_query, data)
        self.conn.commit()
        print("Records inserted successfully..")
        self.close()

    def update_customer(self):
        self.get_all_customers()
        try:
            customer_id = int(input("Enter customerID to be updated: "))
            customer = Customer()
            try:
                first_name = input("Enter First Name of Customer: ")
                if authenticate_customer_(first_name):
                    customer.set_first_name(first_name)
            except InvalidDataException as e:
                print(f'Invalid Input: {e}')
            try:
                last_name = input("Enter Last Name of Customer: ")
                if authenticate_customer_(last_name):
                    customer.set_last_name(last_name)
            except InvalidDataException as e:
                print(f'Invalid Input: {e}')
                return
            customer.set_email(input("Enter Email of Customer: "))
            try:
                phone_number = input("Enter Phone Number of Customer: ")
                if authenticate_phone(phone_number):
                    customer.set_phone_number(phone_number)
            except InvalidDataException as e:
                print(f'Invalid Input: {e}')
                return
            customer.set_address(input("Enter Address: "))
            update_str = ('''
                    UPDATE Customers SET FirstName=%s, LastName=%s, Email=%s, Phone=%s, Address=%s WHERE customerID=%s;
                    ''')
            self.open()
            data = [customer.get_first_name(), customer.get_last_name(), customer.get_email(), customer.get_phone_number(),
                    customer.get_address(), customer_id]
            try:
                self.open()
                self.stmt.executemany(update_str, data)
                self.conn.commit()
                print("Records Updated Successfully...")
            except Exception as e:
                self.conn.rollback()
                print(f"Error: {e}")
            finally:
                self.close()
        except Exception as e:
            print(e)

    def delete_customer(self):
        try:
            self.open()
            select_query = "SELECT * FROM Customers WHERE customerID = %s"
            Id = int(input("Enter customerID to be deleted: "))
            self.stmt.execute(select_query, (Id,))
            customer_data = self.stmt.fetchone()
            if customer_data:
                delete_str = f'DELETE FROM Customers WHERE customerID={Id};'
                self.open()
                self.stmt.execute(delete_str)
                self.conn.commit()
                print("Records Deleted Successfully...")
                self.close()
            else:
                raise InvalidDataException("customerID not found in Database...")
        except InvalidDataException as e:
            print(f"Customer Deletion Failed: {e}")

    def get_customer_by_id(self):
        try:
            self.open()
            customer_id = int(input("Enter CustomerId to get details: "))
            cus_str = f'SELECT * FROM Customers WHERE CustomerId={customer_id};'
            self.stmt.execute(cus_str)
            records = self.stmt.fetchall()
            self.conn.commit()
            if records:
                print()
                print("...............Customer Details for customerID: ", customer_id, "...............")
                for i in records:
                    print(i)
                print()
                self.close()
            else:
                raise InvalidDataException("customerID not found in Database...")
        except InvalidDataException as e:
            print(f"Customer Not Found: {e}")

    def get_all_customers(self):
        self.open()
        select_str = 'SELECT * FROM Customers;'
        self.stmt.execute(select_str)
        records = self.stmt.fetchall()
        print()
        print("...............Records in Table...............")
        for i in records:
            print(i)
        print()
        self.close()

    def calculate_total_orders(self):
        self.open()
        CustomerID = int(input("Enter CustomerID to Calculate Total Orders: "))
        query = f"SELECT COUNT(*) FROM Orders WHERE CustomerID = {CustomerID};"
        self.stmt.execute(query)
        total_orders = self.stmt.fetchone()[0]
        print(f'Total Orders placed by {CustomerID} : {total_orders}')
        self.close()

    def get_customer_details(self):
        try:
            customer_id = int(input("Enter CustomerId to get details: "))
            self.open()
            cus_str = f'SELECT * FROM Customers WHERE CustomerId={customer_id};'
            self.stmt.execute(cus_str)
            records = self.stmt.fetchall()
            self.conn.commit()
            if records:
                print()
                print("...............Customer Details for customerID: ", customer_id, "...............")
                for i in records:
                    print(f"CustomerID: {i[0]}, FirstName: {i[1]}, LastName: {i[2]}, Email: {i[3]}, Phone: {i[4]}, Address: {i[5]}")
                print()
                self.close()
            else:
                raise AuthenticationException("customerID not found in Database...")
        except AuthenticationException as e:
            print(f"Invalid Input : {e}")

    def update_customer_info(self):
        try:
            Id = int(input("Enter customerID to be deleted: "))
            select_query = f"SELECT * FROM Customers WHERE customerID = {Id}"
            self.open()
            self.stmt.execute(select_query)
            customer_data = self.stmt.fetchone()
            if customer_data:
                customer = Customer()
                try:
                    first_name = input("Enter First Name of Customer: ")
                    if authenticate_customer_(first_name):
                        customer.set_first_name(first_name)
                except InvalidDataException as e:
                    print(f'Invalid Input: {e}')
                try:
                    last_name = input("Enter Last Name of Customer: ")
                    if authenticate_customer_(last_name):
                        customer.set_last_name(last_name)
                except InvalidDataException as e:
                    print(f'Invalid Input: {e}')
                customer.set_email(input("Enter Email of Customer: "))
                try:
                    phone_number = input("Enter Phone Number of Customer: ")
                    if authenticate_phone(phone_number):
                        customer.set_phone_number(phone_number)
                except InvalidDataException as e:
                    print(f'Invalid Input: {e}')
                customer.set_address(input("Enter Address: "))
                update_str = ('''
                UPDATE Customers SET FirstName=%s, LastName=%s, Email=%s, Phone=%s, Address=%s WHERE CustomerID=%s;
                ''')
                self.open()
                data = [customer.get_first_name(), customer.get_last_name(), customer.get_email(), customer.get_phone_number(),
                        customer.get_address(), Id]
                self.stmt.execute(update_str, data)
                self.conn.commit()
                print("Records Updated Successfully...")
                self.close()
        except InvalidDataException as e:
            print(f'Invalid Input: {e}')
