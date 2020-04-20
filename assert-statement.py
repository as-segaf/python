#!/usr/bin/python3.8

## Python assert statement is one which assert or test the trueness of a condition in your code
## This is debugging tool
## If it is true, move over the next line of code
## If it is false, stop all operations and throw an error

# assert 2==3

def div(arg1,arg2):
    assert arg2!=0
    return print(arg1/arg2)

div(3,2)
# div(3,0)

## Using an error message

def div(arg1,arg2):
    assert arg2!=0, "You cannot divide a number by 0\n Please try again"
    return print(arg1/arg2)

# div(3,0)

## Using try block
## This is not gonna work
try:
    def div(a,b):
        assert b!=0, "You cannot divide a number by 0\n Please try again"
        return print(a/b)
except:
    print("So you tried to divide by 0, please try again")

# div(1,0)

## Try this one

def div(a,b):
    try:
        assert b!=0, "You cannot divide a number by 0\n Please try again"
        return print(a/b)
    except:
        print("So you tried to divide by 0, please try again")

div(1,0)
