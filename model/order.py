

class Order:
    def __init__(self, orderID, customer, employee, shipper, OrderDate):
        self.orderID = orderID
        self.customerID = customer.customerID
        self.employeeID = employee.employeeID
        self.shipperID = shipper.shipperID
        self.OrderDate = OrderDate


    # getter method
    def get_orderID(self):
        return self.orderID

    # getter method
    def get_customerID(self):
        return self.customerID

    # getter method
    def get_employeeID(self):
        return self.employeeID

    # getter method
    def get_shipperID(self):
        return self.shipperID

    # getter method
    def get_OrderDate(self):
        return self.OrderDate


    # setter method
    def set_orderID(self, orderID):
        self.orderID = orderID

    # setter method
    def set_customerID(self, customerID):
        self.customerID = customerID

    # setter method
    def set_employeeID(self, employeeID):
        self.employeeID = employeeID

    # setter method
    def set_shipperID(self, shipperID):
        self.shipperID = shipperID

    # setter method
    def set_OrderDate(self, OrderDate):
        self.OrderDate = OrderDate

    def get_infor(self):
        return self.orderID + "," + self.customerID + "," + self.employeeID + "," + self.shipperID + "," + self.OrderDate + "."

    def get_infor_dist(self):
        return {
            "categoryID": self.orderID,
            "customerID": self.customerID,
            "description": self.employee,
            "shipper": self.shipper,
            "OrderDat": self.OrderDat
        }