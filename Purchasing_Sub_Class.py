from Listings_Super_Class import Listings
import random


class Purchasing(Listings):
    def __init__(self, product_name, product_num, product_price, sold_by, quantity=0, order_num=0,
                 purchase_total=0, date=""):
        super().__init__(product_name, product_num, product_price, sold_by)
        self._quantity = quantity
        self._order_num = order_num
        self._purchase_total = purchase_total
        self._date = date

    def __repr__(self):
        gang = "\nQuantity: " + str(self._quantity) + "\nOrder Number: " + str(self._order_num) + \
               "\nPurchase Total: " + str(self._purchase_total) + "\nDate: " + str(self._date)
        return gang

    @property
    def get_quantity(self):
        return self._quantity

    @property
    def get_order_num(self):
        return self._order_num

    @property
    def get_purchase_total(self):
        return self._purchase_total

    @property
    def get_date(self):
        return self._date

    def set_quantity(self):
        quan_to_set = int(input("How many would you like to purchase?: "))
        self._quantity = quan_to_set

    def set_order_num(self):
        self._order_num = random.randint(1000, 9999)

    def set_purchase_total(self):
        self._purchase_total = self._quantity * self.get_product_price

    def set_date(self, date_to_set):
        self._date = date_to_set
