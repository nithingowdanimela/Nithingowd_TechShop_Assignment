class OrderDetails:
    def __init__(self, order_detail_id=None, order_id=None, product_id=None, quantity=None):
        self.__order_detail_id = order_detail_id
        self.__order_id = order_id
        self.__product_id = product_id
        self.__quantity = quantity

    # Getters
    def get_order_detail_id(self):
        return self.__order_detail_id

    def get_order_id(self):
        return self.__order_id

    def get_product_id(self):
        return self.__product_id

    def get_quantity(self):
        return self.__quantity

    # Setters
    def set_order_detail_id(self, order_detail_id):
        self.__order_detail_id = order_detail_id

    def set_order_id(self, order_id):
        self.__order_id = order_id

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def set_quantity(self, quantity):
        self.__quantity = quantity
