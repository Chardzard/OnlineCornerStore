from Purchasing_Sub_Class import Purchasing


class Shipping_Info(Purchasing):
    def __init__(self, product_name, product_num, product_price, sold_by, quantity, order_num, purchase_total, date,
                 first_name="", last_name="", address="", phone_num="", email=""):
        super().__init__(product_name, product_num, product_price, sold_by, quantity, order_num, purchase_total, date)
        self._first_name = first_name
        self._last_name = last_name
        self._address = address
        self._phone_num = phone_num
        self._email = email

    def __repr__(self):
        print("\n")
        shipment_info = self._first_name + " " + self._last_name + ", thank you for your order #" + \
            str(self._order_num) + ". Your item will be shipped to \n" + self._address + " as soon as possible. " + \
            "Check either the phone or email below for updates." + "\nPhone: " + self._phone_num + \
            "\nEmail: " + self._email
        return shipment_info

    @property
    def get_first_name(self):
        return self._first_name

    @property
    def get_last_name(self):
        return self._last_name

    @property
    def get_address(self):
        return self._address

    @property
    def get_phone_num(self):
        return self._phone_num

    @property
    def get_email(self):
        return self._email

    def set_first_name(self):
        name_to_set = str(input("Enter first name: "))
        self._first_name = name_to_set

    def set_last_name(self):
        name_to_set = str(input("Enter last name: "))
        self._last_name = name_to_set

    def set_address(self):
        address_to_set = str(input("Enter shipping address: "))
        self._address = address_to_set

    def set_phone_num(self):
        phone_to_set = str(input("Enter phone number: "))
        self._phone_num = phone_to_set

    def set_email(self):
        email_to_set = str(input("Enter email: "))
        self._email = email_to_set
