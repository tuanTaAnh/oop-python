from model.orderdetails import *

class OrderDetailDAO:
    def __init__(self):
       self.orddeList =  []

    def add_orderdetail(self, orderdetailID, orderID, productID, quatity):
        assert self.__check_unique_id(orderdetailID), "The id is not unique"

        ord_det = OrderDetail(orderdetailID, orderID, productID, quatity)
        self.orddeList.append(ord_det)


    def get_orderdetail_by_id(self, id):
        for ord_det in self.orddeList:
            if ord_det.orderdetailID == id:
                return ord
        return None

    def print_orderdetaildlist(self):
        print("LIST OF ORDER DETAILS: ")
        for ord_det in self.orddeList:
            print(ord_det.get_infor())
        print()


    def __check_unique_id(self, id):
        for ord_det in self.orddeList:
            if ord_det.orderdetailID == id:
                return False
        return True
