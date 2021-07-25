from model.order import *

class OrderDAO:
    def __init__(self):
       self.odrList =  []

    def add_order(self, orderID, customer, employee, shipper, OrderDate):
        assert self.__check_unique_id(orderID), "The id is not unique"

        ord = Order(orderID, customer, employee, shipper, OrderDate)
        self.odrList.append(ord)


    def get_ord_by_id(self, id):
        for ord in self.odrList:
            if ord.orderID == id:
                return ord
        return None

    def print_ordlist(self):
        print("LIST OF ORDERS: ")
        for ord in self.odrList:
            print(ord.get_infor())
        print()


    def __check_unique_id(self, id):
        for ord in self.odrList:
            if ord.orderID == id:
                return False
        return True
