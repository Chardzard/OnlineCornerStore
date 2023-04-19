import random


class Listings:
    def __init__(self, product_name="", product_num=0, product_price=0, sold_by=""):
        self._product_name = product_name
        self._product_num = product_num
        self._product_price = product_price
        self._sold_by = sold_by

    def __repr__(self):
        gang = "Listing Name: " + self._product_name + "\nListing ID: " + str(self._product_num) + "\nListing Price: " \
               + str(self._product_price) + "\nSold By: " + self._sold_by
        return gang

    @property
    def get_product_name(self):
        return self._product_name

    @property
    def get_product_num(self):
        return self._product_num

    @property
    def get_product_price(self):
        return self._product_price

    @property
    def get_sold_by(self):
        return self._sold_by

    def set_product_name(self, name_to_set):
        self._product_name = name_to_set

    def set_product_num(self):
        self._product_num = random.randint(100, 9999)

    def set_product_price(self, price_to_set):
        self._product_price = price_to_set

    def set_sold_by(self, seller):
        self._sold_by = seller
