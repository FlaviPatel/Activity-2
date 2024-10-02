 # Write a program to create a class with name Student and perform the following tasks - Declare a variable  name andgrade Print a sentence inside the class Create an object of class student and see the output
class Student:
    # Attribute
    name = "Tia"
    grade = 9

    # Method
    def display(self):
        print("Student name is", self.name)
        print("Student grade is", self.grade)

# MAIN PROGRAM
# Create an object
student1 = Student()
student1.display() 
 


