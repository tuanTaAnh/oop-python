

class Product:
    def __init__(self, productID, productName, supplier, category, unit, price):
        self.productID = productID
        self.productName = productName
        self.supplierID = supplier.supplierID
        self.categoryID = category.categoryID
        self.unit = unit
        self.price = price


    # getter method
    def get_productID(self):
        return self.productID

    # getter method
    def get_productName(self):
        return self.productName

    # getter method
    def get_supplierID(self):
        return self.supplierID

    # getter method
    def get_categoryID(self):
        return self.categoryID

    # getter method
    def get_unit(self):
        return self.unit

    # getter method
    def get_price(self):
        return self.price


    # setter method
    def set_productID(self, productID):
        self.orderID = productID

    # setter method
    def set_productName(self, productName):
        self.productName = productName

    # setter method
    def set_supplierID(self, supplierID):
        self.supplierID = supplierID

    # setter method
    def set_categoryID(self, categoryID):
        self.categoryID = categoryID

    # setter method
    def set_unit(self, unit):
        self.unit = unit

    # setter method
    def set_price(self, price):
        self.unit = price

    def get_infor(self):
        return self.productID + ", " + self.productName + ", " + self.supplierID + ", " + self.categoryID + ", " + str(self.unit) + ", " + str(self.price) + "."