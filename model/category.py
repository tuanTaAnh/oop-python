
class Category:
    def __init__(self, categoryID, categoryName, description):
        self.categoryID = categoryID
        self.categoryName = categoryName
        self.description = description


    # getter method
    def get_categoryID(self):
        return self.categoryID

    # getter method
    def get_categoryName(self):
        return self.categoryName

    # getter method
    def get_description(self):
        return self.description


    # setter method
    def set_categoryID(self, categoryID):
        self.categoryID = categoryID

    # setter method
    def set_categoryName(self, categoryName):
        self.categoryName = categoryName

    # setter method
    def set_description(self, description):
        self.description = description


    def get_infor(self):
        return self.categoryID + "," + self.categoryName + ","  + self.description + "."

    def get_infor_dist(self):
        return {
            "categoryID": self.categoryID,
            "categoryName": self.categoryName,
            "description": self.description,
        }