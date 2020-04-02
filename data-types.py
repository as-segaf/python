#!/usr/bin/python3.8

## python string

stri = "hello world !"

# str[0]="t"                                                  # error, string cannot be changed
print(f"string {stri} asfkasf")
print(str)                                                  # hello world !
print(str[0])                                               # h
print(str[2:5])                                             # llo 
print(str[2:])                                              # llo world !
print(str * 2 )                                             # hello world !hello world !
print(str + " testing")                                     # hello world ! testing
print("My name is %s and weight is %d kg" % ('john',21))    # My name is john and weight is 21 kg
print('\n')

## python lists (similar to array)
# use square brackets []
# elements and size can be changed

list = ['testing', 123, 1.58, 'hello']
tinylist = [345, 'world']

print('lists')
print(list)             # ['testing', 123, 1.58, 'hello']
print(list[0])          # testing
print(list[0:2])        # ['testing', 123]
print(list[1:])         # ['123', 1.58, 'hello']
print(tinylist * 2)     # [345, 'world', 345, 'world'] 
print(list + tinylist)  # ['testing', 123, 1.58, 'hello', 345, 'world']

del list[0]

print(list)             # [123, 1.58, 'hello']
print('\n')

## python tuples
# use parentheses ()
# elements and size cannot be updated
# can be thought of as "read-only" lists

tuple = ('qwe', 123, 34.5, 'jhon', 98.7)
tinytuple = (432, 'test')

print('tuple')
print(tuple)                # ('qwe', 123, 34.5, 'jhon', 98.7)
print(tuple[0])             # 'qwe'
print(tuple[0:2])           # ('qwe', 123, 34.5)
print(tuple[1:])            # (123, 34.5, 'jhon', 98.7)
print(tuple * 3)            # ('qwe', 123, 34.5, 'jhon', 98.7, 'qwe', 123, 34.5, 'jhon', 98.7, 'qwe', 123, 34.5, 'jhon', 98.7)
print(tuple + tinytuple)    # ('qwe', 123, 34.5, 'jhon', 98.7, 432, 'test')
print('\n')

list[1] = 999       # valid syntax with list
print(list[1])
print('\n')
tuple[1] = 999      # invalid syntax with tuple

## python dictionary (similar to object)
# use curl braces {}

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'job': 'pilot'}

print (dict['one'])       # "This is one"
print (dict[2])           # "This is two"
print (tinydict)          # {'name': 'john','code':6734, 'job': 'pilot'}
print (tinydict.keys())   # dict_keys(['code', 'ame', 'job'])
print (tinydict.values()) # dict_values([6734, 'john', 'pilot'])
