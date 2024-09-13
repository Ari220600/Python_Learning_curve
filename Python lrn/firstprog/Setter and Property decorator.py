
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

Samrat_Basak = Employee("Samrat", "Basak")
# Sarthak_Das = Employee("Sarthak", "Das")

print(Samrat_Basak.email)

Samrat_Basak.fname = "Fitz"

print(Samrat_Basak.email)
Samrat_Basak.email = "this.that@gmail.com"
print(Samrat_Basak.fname)

del Samrat_Basak.email
print(Samrat_Basak.email)
Samrat_Basak.email = "Samrat.Fitz@gmail.com"
print(Samrat_Basak.email)

