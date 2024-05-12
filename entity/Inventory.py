class Inventory:
    def __init__(self, inventory_id=None, product=None, quantity_in_stock=None, last_stock_update=None):
        self.__inventory_id = inventory_id
        self.__product = product
        self.__quantity_in_stock = quantity_in_stock
        self.__last_stock_update = last_stock_update

    # Getters
    def get_inventory_id(self):
        return self.__inventory_id

    def get_product(self):
        return self.__product

    def get_quantity_in_stock(self):
        return self.__quantity_in_stock

    def get_last_stock_update(self):
        return self.__last_stock_update

    # Setters
    def set_inventory_id(self, inventory_id):
        self.__inventory_id = inventory_id

    def set_product(self, product):
        self.__product = product

    def set_quantity_in_stock(self, quantity_in_stock):
        self.__quantity_in_stock = quantity_in_stock

    def set_last_stock_update(self, last_stock_update):
        self.__last_stock_update = last_stock_update
