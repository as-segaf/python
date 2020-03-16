#!/usr/bin/python3

## function
# function start with the keyword def followed by function name and parentheses ()
# the first statement of a function can be optional statement, the documentation string of the function
# or docstring

def testing(string):
    "this function prints a given string"
    print(string)
    return

testing("hello world !!!")

def changeme(myList):
    "this function append the given list with some numbers"
    myList.append(1)
    print("Values inside the function:", myList)
    return

myList = [10,20,30]
changeme(myList)
print("Values outside the function:", myList)

def changeme(myList):
    "this function changes the given list"
    myList = [1,2,3,4]
    print("Values inside the function:", myList)
    return

myList = [9,8,7]
changeme(myList)
print("Values outside the function:", myList)
    

# required arguments
def printme(str):
    print(str)
    return

# printme()   # TypeError: printme() takes exactly 1 argument (0 given)

# keyword arguments
def printme(str):
    print(str)
    return

printme(str = "hello")  # 'hello'

# default arguments
def printinfo(name,age=50):
    print("name:",name)
    print("age:",age)

printinfo(name='agus')

# variable-lenght arguments
def printinfo(arg1, *nextArg):
    print("the output is:")
    print(arg1)
    for var in nextArg:
        print(var)
    return

print(10)
print(1,2,3,4)

# anonymous function
sum = lambda arg1, arg2: arg1 + arg2

print("value total is:",sum(10,20))
print("value total is:",sum(40,20))

# return

def sum(arg1,arg2):
    total = arg2 + arg1
    print("value inside the function:", total)
    return total

numbers = sum(25,20)
print('value outside the function:',numbers)