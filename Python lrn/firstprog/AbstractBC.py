
# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self,l,b):
        self.length = l
        self.breadth = b

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle(10,6)
print(rect1.printarea())

