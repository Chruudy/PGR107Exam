
class Student:
    # Class variable
    passingMark = 50

    def __init__(self, name, mark):
        # Instance variables unique to each instance
        self.name = name
        self.mark = mark

    def __str__(self):
        # This method returns the string representation of the object
        return f"Name: {self.name}, Mark: {self.mark}"

    def passOrFail(self):
        # This method checks if the student's mark is at least the passing mark
        if self.mark >= Student.passingMark:
            return "Pass"
        else:
            return "Fail"


# Instantiate a Student object with name 'John' and mark 52

student1 = Student(name='John', mark=52)

# Print John's pass or fail status
print(f"{student1.name}'s Status: {student1.passOrFail()}")

# Instantiate another Student object with name 'Jenny' and mark 69
student2 = Student(name='Jenny', mark=69)

# Print Jenny's pass or fail status
print(f"{student2.name}'s Status: {student2.passOrFail()}")
