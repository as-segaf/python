#!/usr/bin/python3.8

## Decorators is functions that adds functionallity to another
## but does not modify it
## Python decorator wraps another function 

def func1():
    print("hi")

def func2(arg1):
    def func3():
        print("hello")
        arg1()
        print("hello")
    return func3

newFunc = func2(func1)
newFunc()

## Why use a nested function??

def func1():
    print("hi")

def func2(arg1):
    print("hello")
    arg1()
    print("hello")

# we didn't call newFunc, but look what happen
newerFunc = func2(func1)
# look what happen when we call newFunc
newerFunc()


## Decorators with parameters

def divide(a,b):
    return a/b

def func2(arg1):
    def func3(a,b):
        if b==0:
            print("can't divide by 0")
            return
        print(arg1(a,b))
    return func3

newFunc = func2(divide)
newFunc(1,2)

## Pie syntax

def func2(arg1):
    print("hello")
    arg1()
    print("hello")

@func2
def func1():
    print("hi")


## Chaining decorators

def func3(arg):
    def justFunc():
        print("hello")
        arg1()
        print("hello")
    return justFunc()

def func2(arg):
    def justFunc():
        print("world")
        arg2()
        print("world")
    return justFunc

@func3
@func2
def func1():
    print("hi")