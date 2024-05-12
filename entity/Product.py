class Product:
    def __init__(self, product_id=None, product_name=None, desc=None, price=None):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__desc = desc
        self.__price = price

    # Getters
    def get_product_id(self):
        return self.__product_id

    def get_product_name(self):
        return self.__product_name

    def get_desc(self):
        return self.__desc

    def get_price(self):
        return self.__price

    # Setters
    def set_product_id(self, product_id):
        self.__product_id = product_id

    def set_product_name(self, product_name):
        self.__product_name = product_name

    def set_desc(self, desc):
        self.__desc = desc

    def set_price(self, price):
        self.__price = price
