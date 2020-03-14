#!/usr/bin/python3

# break

for letter in 'Python':
    if letter == 't':
        break
    print('Current letter:',letter)

num = 10
while num > 0:
    print('Current number is:',num)
    num -= 1
    if num == 5:
        break

input = int(input('enter any number:'))
numbers = [1,2,3,4,5]
for number in numbers:
    if input == number:
        print('number found in list')
        break
else:
    print('number not found in list')

# continue

for letter in 'Python':
    if letter == 'h':
        continue
    print('Current letter is:',letter)

num = 10
while num > 0:
    num -= 1
    if num == 5:
        continue
    print('Current value:',num)

# pass 
# pass is just a placeholder for
# functionality to be added later.
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass