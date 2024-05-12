from dao.CustomerService import CustomerService
from dao.ProductService import ProductService
from dao.OrderService import OrderService
from dao.OrderDetailsService import OrderDetailsService
from dao.InventoryService import InventoryService
from exception.InvaliDataException import InvalidDataException


class Main:
    def __init__(self):
        self.loop = None

    def main(self):
        self.loop = True
        while self.loop:
            try:
                customerservice = CustomerService()
                productservice = ProductService()
                orderservice = OrderService()
                orderdetailservice = OrderDetailsService()
                inventoryservice = InventoryService()
                print("Welcome to TechShop!!!")
                print("Select option to use functionalities: ")
                print("1.Customer\n2.Product\n3.Order\n4.Order Details\n5.Inventory\n6.Exit")
                choice = int(input("Enter your choice: "))
                if str(choice) in "123456":
                    if choice == 1:
                        while True:
                            print('''1.Register Customer\n2.Update Customer\n3.Delete Customer\n4.Get Customer by ID
5.Get All Customers\n6.Calculate Total Orders\n7.Exit
                            ''')
                            choice_1 = int(input("Enter your Choice: "))
                            if str(choice_1) in "1234567":
                                if choice_1 == 1:
                                    customerservice.register_customer()
                                elif choice_1 == 2:
                                    customerservice.update_customer_info()
                                elif choice_1 == 3:
                                    customerservice.delete_customer()
                                elif choice_1 == 4:
                                    customerservice.get_customer_details()
                                elif choice_1 == 5:
                                    customerservice.get_all_customers()
                                elif choice_1 == 6:
                                    customerservice.calculate_total_orders()
                                else:
                                    break
                            else:
                                raise InvalidDataException("Input should be between 1 and 7")
                    elif choice == 2:
                        while True:
                            print('''1.Add Product\n2.Update Product\n3.Remove Product\n4.Get Product details by ID
5.Get All Products\n6.To Check Product in Stock\n7.Exit
                            ''')
                            choice_2 = int(input("Enter your Choice: "))
                            if str(choice_2) in "1234567":
                                if choice_2 == 1:
                                    productservice.add_product()
                                elif choice_2 == 2:
                                    productservice.update_product_info()
                                elif choice_2 == 3:
                                    productservice.remove_product()
                                elif choice_2 == 4:
                                    productservice.get_product_details()
                                elif choice_2 == 5:
                                    productservice.get_all_products()
                                elif choice_2 == 6:
                                    productservice.is_product_in_stock()
                                else:
                                    break
                            else:
                                raise InvalidDataException("Input should be between 1 and 6")
                    elif choice == 3:
                        while True:
                            print('''1.Create Order\n2.Update Order Status\n3.Cancel Order\n4.Get Order by ID
5.To Calculate Total Amount\n6.Get All Orders\n7.Exit
                            ''')
                            choice_3 = int(input("Enter your Choice: "))
                            if str(choice_3) in "1234567":
                                if choice_3 == 1:
                                    orderservice.add_order()
                                elif choice_3 == 2:
                                    orderservice.update_order_status()
                                elif choice_3 == 3:
                                    orderservice.cancel_order()
                                elif choice_3 == 4:
                                    orderservice.get_order_details()
                                elif choice_3 == 5:
                                    orderservice.calculate_total_amount()
                                elif choice_3 == 6:
                                    orderservice.get_all_orders()
                                else:
                                    break
                            else:
                                raise InvalidDataException("Input should be between 1 and 7")
                    elif choice == 4:
                        while True:
                            print('''1.Add Order Detail\n2.Update Order Detail\n3.Remove Order Detail\n4.Get Order Detail by ID
5.Get All Order Details\n6.To calculate SubTotal\n7.Update Quantity\n8.Add Discount\n9.Exit
                            ''')
                            choice_4 = int(input("Enter your Choice: "))
                            if str(choice_4) in "123456789":
                                if choice_4 == 1:
                                    orderdetailservice.add_order_detail()
                                elif choice_4 == 2:
                                    orderdetailservice.update_order_detail()
                                elif choice_4 == 3:
                                    orderdetailservice.remove_order_detail()
                                elif choice_4 == 4:
                                    orderdetailservice.get_order_detail_info()
                                elif choice_4 == 5:
                                    orderdetailservice.get_all_order_details()
                                elif choice_4 == 6:
                                    orderdetailservice.calculate_subtotal()
                                elif choice_4 == 7:
                                    orderdetailservice.update_quantity()
                                elif choice_4 == 8:
                                    orderdetailservice.add_discount()
                                else:
                                    break
                            else:
                                raise InvalidDataException("Input should be between 1 and 9")
                    elif choice == 5:
                        while True:
                            print('''1.Add Inventory\n2.Update Inventory\n3.Remove Inventory\n4.Get Inventory by ProductID
5.Get All Inventory\n6.Get Quantity In Stock\n7.Quantities to Add into Inventory\n8.Quantities to Remove from Inventory\n9.Update Stock Quantity\n10.List Available Products
11.To get Total Cost of Inventory\n12.List Low Stock Products\n13.List Out of Stock Products\n14.List All Products\n15.Exit
                            ''')
                            choice_5 = int(input("Enter your Choice: "))
                            if str(choice_5) in "123456789101112131415":
                                if choice_5 == 1:
                                    inventoryservice.add_inventory()
                                elif choice_5 == 2:
                                    inventoryservice.update_inventory()
                                elif choice_5 == 3:
                                    inventoryservice.remove_inventory()
                                elif choice_5 == 4:
                                    inventoryservice.get_product()
                                elif choice_5 == 5:
                                    inventoryservice.get_all_inventory()
                                elif choice_5 == 6:
                                    inventoryservice.get_quantity_in_stock()
                                elif choice_5 == 7:
                                    inventoryservice.add_to_inventory()
                                elif choice_5 == 8:
                                    inventoryservice.remove_from_inventory()
                                elif choice_5 == 9:
                                    inventoryservice.update_stock_quantity()
                                elif choice_5 == 10:
                                    inventoryservice.is_product_available()
                                elif choice_5 == 11:
                                    inventoryservice.get_inventory_value()
                                elif choice_5 == 12:
                                    inventoryservice.list_low_stock_products()
                                elif choice_5 == 13:
                                    inventoryservice.list_out_of_stock_products()
                                elif choice_5 == 14:
                                    inventoryservice.list_all_products()
                                else:
                                    break
                            else:
                                raise InvalidDataException("Input should be between 1 and 15")
                    else:
                        exit()
                else:
                    raise InvalidDataException("Input should be between 1 and 6")
            except InvalidDataException as e:
                print(f"Invalid input: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                print("Thank You for reaching TechShop...")


obj = Main()
obj.main()
