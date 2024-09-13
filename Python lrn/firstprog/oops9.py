
class Dad:
    basketball =6

class Son(Dad):
    dance =1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance =6
    guitar = 1

    def isdance(self):
        return f"Jackson yeah!" \
            f"Yes I dance very awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
harry = Grandson()

# print(darry.guitar)

# electronic device
# pocket gadget
# phone



class ElectronicDevice:
    cost ="My cost is 600"
    me="I am an Electronic device"
    def canrun(self):
        return "I can run hard calculations"

class PocketGadget(ElectronicDevice):
    cost = "My cost is 800"
    me = "I am a Pocket gadget"
    def canrun(self):
        return f"{ElectronicDevice.canrun(self)} and also send and recieve calls"

class phone(PocketGadget):
    cost = "My cost is 2000"
    me = "I am a Phone"
    def canrun(self):
        return  f"{PocketGadget.canrun(self)}. I can also run Internet."

calculator = ElectronicDevice()
Pager = PocketGadget()
Mobile = phone()

print(calculator.me)
print(calculator.canrun())
print(calculator.cost)

print(Pager.me)
print(Pager.canrun())
print(Pager.cost)

print(Mobile.me)
print(Mobile.canrun())
print(Mobile.cost)