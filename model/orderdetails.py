

class OrderDetail:
    def __init__(self, orderdetailID, order, product, quatity):
        self.orderdetailID = orderdetailID
        self.orderID = order.orderID
        self.productID = product.productID
        self.quatity = quatity


    # getter method
    def get_orderdetailID(self):
        return self.orderdetailID

    # getter method
    def get_orderID(self):
        return self.orderID

    # getter method
    def get_productID(self):
        return self.productID

    # getter method
    def get_quatity(self):
        return self.quatity


    # setter method
    def set_orderdetailID(self, orderdetailID):
        self.orderdetailID = orderdetailID

    # setter method
    def set_orderID(self, orderID):
        self.orderID = orderID

    # setter method
    def set_productID(self, productID):
        self.productID = productID

    # setter method
    def set_quatity(self, quatity):
        self.quatity = quatity

    def get_infor(self):
        return self.orderdetailID + ", " + self.orderID + ", " + self.productID + ", " + str(self.quatity) +  "."