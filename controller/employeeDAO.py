from model.employee import *

class EmployeeDAO:
    def __init__(self):
       self.employList =  []

    def add_employee(self, employID, lastname, firstname, birthdate, photos, notes):
        assert self.__check_unique_id(employID), "The id is not unique"

        emp = Employee(employID, lastname, firstname, birthdate, photos, notes)
        self.employList.append(emp)

    def get_emp_by_id(self, id):
        for emp in self.employList:
            if emp.employeeID == id:
                return emp
        return None

    def print_emplist(self):
        print("LIST OF EMPLOYEES: ")
        for emp in self.employList:
            print(emp.get_infor())
        print()


    def __check_unique_id(self, id):
        for emp in self.employList:
            if emp.employeeID == id:
                return False
        return True