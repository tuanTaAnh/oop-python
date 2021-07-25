
class Employee:
    def __init__(self, employID, lastname, firstname, birthdate, photos, notes):
        self.employeeID = employID
        self.lastname = lastname
        self.firstname = firstname
        self.birthdate = birthdate
        self.photos = photos
        self.notes = notes

    # getter method
    def get_employeeID(self):
        return self.employeeID

    # getter method
    def get_lastname(self):
        return self.lastname

    # getter method
    def get_firstname(self):
        return self.firstname

    # getter method
    def get_birthdate(self):
        return self.birthdate

    # getter method
    def get_photos(self):
        return self.photos

    # getter method
    def get_notes(self):
        return self.notes

    # setter method
    def set_employeeID(self, employeeID):
        self.employeeID = employeeID

    # setter method
    def set_lastname(self, lastname):
        self.lastname = lastname

    # setter method
    def set_firstname(self, firstname):
        self.firstname = firstname

    # setter method
    def set_birthdate(self, birthdate):
        self.birthdate = birthdate

    # setter method
    def set_photos(self, photos):
        self.photos = photos

    # setter method
    def set_notes(self, notes):
        self.notes = notes

    def get_infor(self):
        return str(self.employeeID) + ", " + self.lastname + ", " \
               + self.firstname + ", " + str(self.birthdate) + ", " + self.photos + ", " + self.notes + "."