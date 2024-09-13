
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    @classmethod
    def from_slash(cls, string):
        # params = string.split("-")
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))


harry = Employee("Harry", 25500, "Instructor")

rohan = Employee("Rohan",45540,"Chief Instructor")

Karan = Employee.from_slash("Karan-40000-Supervisor")
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"

# print(harry.printdetails())
# print(rohan.printdetails())
rohan.change_leaves(10)
# print(harry.no_of_leaves)
print(Karan.salary)