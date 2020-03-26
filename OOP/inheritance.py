#!/usr/bin/python3

class Parent:   # define parent class 
    parentAttr = 100
    def __init__(self):
        print("calling parent constructor")

    def parentMethod(self):
        print("calling parent method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("parent attribute :",Parent.parentAttr)

    def myMethod(self):
        print("this is parent's method")

class Child(Parent):    # define child class
    def __init__(self):
        print("Calling child constructor")
    
    def childMethod(self):
        print("calling child method")

    def myMethod(self):
        print("this is child's method")

## Data hiding
# "__" means private
# "_" means protected

class justCounter():
    __secretCounter = 0     # private member of class

    def count(self):
        self.__secretCounter += 1
        print(self.__secretCounter)

counter = justCounter()
counter.count()     # 1
counter.count()     # 2
# print(counter.__secretCounter)    # error
print(counter._justCounter__secretCounter)  # 2
print('')



c = Child()         # calling child constructor
c.childMethod()     # call child's method
c.parentMethod()    # call parent's method
c.setAttr(500)      # set attr to 500
c.getAttr()         # parent attribute : 500
c.myMethod()        # this is child's method