class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 45550
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 22133
rohan.role = "Student"

print(Employee.no_of_leaves)
# print(Employee.__dict__)
Employee.no_of_leaves = 9
# print(Employee.__dict__)
print(Employee.no_of_leaves)

