#Parent/Base class
class Person:
    def __init__(self, fname, lname, age):
        # Constructor for the Person class
        self.fname = fname
        self.lname = lname
        self.age = age

    def get_info (self):
        # Method to print information about the person
        print ("Full Name:", self.fname, self.lname)
        print ("Age:", self.age)

#Child/Derived class
class Student(Person):
    def __init__(self, fname, lname, age, student_id):
        # Constructor for the Student class
        # Inherite from parent class
        Person.__init__(self, fname, lname, age)
        # Additional attribute for student
        self.student_id = student_id

    # Method to print information about the student
    def get_stuinfo (self):
        # Inherite from parent class
        Person.get_info(self)
        print ("Student ID:", self.student_id)

#Child/Derived class
class Employee(Person):
    def __init__(self, fname, lname, age, employee_number, salary):
        # Constructor for the Employee class
        # Inherite from parent class
        Person.__init__(self, fname, lname, age)
        # Additional attributes for employee
        self.employee_number = employee_number
        self.salary = salary

    # Method to print information about the employee
    def get_empinfo(self):
        # Inherite from parent class
        Person.get_info(self)
        print ("Employee no:", self.employee_number)
        print ("Salary:", self.salary, "USD")

#To check for correct output
new_student = Student ("Anthony", "Smith", 35, "s346571")
new_student.get_stuinfo ()
print ("==========================")
new_employee = Employee ("Sarah", "Tayolr", 34, 2919736, 5000)
new_employee.get_empinfo ()