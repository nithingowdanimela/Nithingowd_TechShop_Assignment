class Order:
    def __init__(self, order_id=None, customer_id=None, order_date=None, total_amount=None):
        self.__order_id = order_id
        self.__customer_id = customer_id
        self.__order_date = order_date
        self.__total_amount = total_amount

    # Getters
    def get_order_id(self):
        return self.__order_id

    def get_customer_id(self):
        return self.__customer_id

    def get_order_date(self):
        return self.__order_date

    def get_total_amount(self):
        return self.__total_amount

    # Setters
    def set_order_id(self, order_id):
        self.__order_id = order_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_order_date(self, date):
        self.__order_date = date

    def set_total_amount(self, phone_number):
        self.__total_amount = phone_number
