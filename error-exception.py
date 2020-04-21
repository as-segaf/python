#!/usr/bin/python3.8


## When we handle the exception, the operation won't stop
## (the code after excepts and finally block will run as expected)

try:
    for i in range(3):
        print(3/i)
except:
    print("You divided by 0")
    print("This prints because the exception was handled")

## Multiple excepts

a,b = 1,0
try:
    print('10'+10)
    print(a/b)
    print("This won't be printed")
except TypeError:
    print("You added the values of incompatible types")
except ZeroDivisionError:
    print("You divided a number by 0")


## Multiple exception in one except
try:
    print('10'+10)
except (ZeroDivisionError,TypeError):
    print('Invalid input')


## A generic except after all excepts

try:
    print('1'+1)    # a TypeError
    print(sum)
    print(2/0)
except NameError:
    print("Sum does not exist")
except ZeroDivisionError:
    print("Cannot divide by 0")
except:
    print("Something wrong")

## There can only be one generic or default except block

try:
    print('1'+1)    # a TypeError
    print(sum)
    print(2/0)
except NameError:
    print("Sum does not exist")
except ZeroDivisionError:
    print("Cannot divide by 0")
except:
    print("Something wrong")
# except:
#     print("this will raise an error")

## Finally block

# try:
#     print(1/0)
# except ValueError:
#     print("This is a value error")
# finally:
#     print("This will print no matter what")

## Exception occurred in except

# try:
#     print(1/0)
# except ZeroDivisionError:
#     print(2/0)
# finally:
#     print("This will print")

## Raise an error keyword

# a,b = 1,0
# if b==0: raise ZeroDivisionError
# print("testing")

## Raise an error keyword with try except block

a,b = 1,0
try:
    if b==0: raise ZeroDivisionError
except:
    print("You try to divide a number by 0")
print("testing")

## Raise without specific exception

# try:
#     print('1'+1)
# except:
#     raise

## Raise with an argument

# try:
#     print('1'+1)
# except:
#     raise ValueError("inappropriate value")

## Define our own exception

class myError(Exception):
    print("This is a problem")

raise myError