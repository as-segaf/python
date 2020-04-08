#!/usr/bin/python3.8

## Using a for loop, we can write:

mylist = []
for i in 'google':
    mylist.append(i)
    
print(mylist)       # ['g','o','o','g','l','e']


## Using list comprehension, we can do this in one line:

print([i for i in 'google'])        # ['g','o','o','g','l','e']
print([i*2 for i in {4,3,2}])       # [4,6,8]

myset = {3,1,2}
print(list(map(lambda i:i,myset)))  # [1,2,3]


# Conditional list comprehension

print([i for i in range(8) if i%2!=0])  # [1,3,5,7]

# Nested conditional

print([i for i in range(8) if i%2==0 if i%3==0])    # [0,6]

# If else

print(["Genap" if i%2==0 else "Ganjil" for i in range(8)])

## Nested for-loop
# Using a regular for-loop

for i in range (7,9):
    for j in range(1,11):
        print(f"{i*j}")

# Using list comprehension

print([[i*j for j in range(1,11)] for i in range(2,4)])

