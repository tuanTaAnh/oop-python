
class Shipper:
    def __init__(self, shipperID, shipperName, Phone):
        self.shipperID = shipperID
        self.shipperName = shipperName
        self.Phone = Phone

    # getter method
    def get_shipperID(self):
        return self.shipperID

    # getter method
    def get_shipperName(self):
        return self.shipperName

    # getter method
    def get_Phone(self):
        return self.Phone

    # setter method
    def set_shipperID(self, shipperID):
        self.shipperID = shipperID

    # setter method
    def set_shipperName(self, shipperName):
        self.shipperName = shipperName

    # setter method
    def set_Phone(self, Phone):
        self.Phone = Phone

    def get_infor(self):
        return str(self.shipperID) + ", " + self.shipperName + ", "  + self.Phone + "."

    def get_infor_dist(self):
        return {
            "shipperID": self.shipperID,
            "shipperName": self.shipperName,
            "Phone": self.Phone
        }