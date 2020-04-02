#!/usr/bin/python3.8

## Global and local scope

total = 0   # this is glbal variable
def sum(arg1,arg2):
    total = arg1 + arg2 # here is local variable
    print('value inside the function:',total)
    return total

sum(10,40)
print("value outside the function:",total)