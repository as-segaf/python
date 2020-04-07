#!/usr/bin/python3.8

## [on_true] if [expressions] else [on_false]
## in C++ it's look like this
## max = (a>b)?a:b

a,b = 2,3
print("a" if a>b else "b")          # b

## (on_false,on_true)[condition]
# Using Tuples

print((b,a)[a>b])                   # 3
print(("salah","benar")[True])      # benar
print((f"b:{b}",f"a:{a}")[a>b])     # b:3

# Using Dictionaries

print({False:b,True:a}[a>b])        # 3
print({True:b,False:a}[a>b])        # 2, if you change the key, it will affect the tenary operations

# Using Lambdas

print((lambda : b, lambda : a)[a>b]())      # 2

## Nested ternary operator

c = 0
print("less than 0" if 0>c else "between 0 and 1" if 1>=c>=0 else "greater than 1")

## Before ternary operators in python
a,b = 2,3
print(a<b and a or b)       # 2

# it checks a<b first
# it returns True
# so it is: True and a or b
# it checks True and a
# it returns a
# so it is: a or b
# it returns a

print(a>b and a or b)       # 3

# it checks a>b first
# it returns False
# so it is: False and a or b
# it checks False and a
# it returns False
# so it is: False or b
# it returns b