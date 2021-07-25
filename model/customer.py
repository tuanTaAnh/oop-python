
class Customer:
    def __init__(self, customerID, customerName, contactName, address, city, postalcode, country):
        self.customerID = customerID
        self.customerName = customerName
        self.contactName = contactName
        self.address = address
        self.city = city
        self.postalcode = postalcode
        self.country = country

    # getter method
    def get_customerID(self):
        return self.customerID

    # getter method
    def get_customerName(self):
        return self.customerName

    # getter method
    def get_contactName(self):
        return self.contactName

    # getter method
    def get_address(self):
        return self.address

    # getter method
    def get_city(self):
        return self.city

    # getter method
    def get_postalcode(self):
        return self.postalcode

    # getter method
    def get_country(self):
        return self.country

    # setter method
    def set_customerID(self, customerID):
        self.customerID = customerID

    # setter method
    def set_customerName(self, customerName):
        self.customerName = customerName

    # setter method
    def set_contactName(self, contactName):
        self.contactName = contactName

    # setter method
    def set_address(self, address):
        self.address = address

    # setter method
    def set_city(self, city):
        self.city = city

    # setter method
    def set_postalcode(self, postalcode):
        self.postalcode = postalcode

    # setter method
    def set_country(self, country):
        self.country = country

    def get_infor(self):
        return self.customerName + "," + self.contactName + "," \
               + self.address + "," + self.city + "," + self.country + "," + self.postalcode + "."

    def get_infor_dist(self):
        return {
            "customerID": self.customerID,
            "customerName": self.customerName,
            "contactName": self.contactName,
            "address": self.address,
            "city": self.city,
            "country":self.country,
             "postalcode":  self.postalcode
        }