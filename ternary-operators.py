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