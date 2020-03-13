#!/usr/bin/python3

# while loop
# loop if comndition is true

count = 0
while (count<9):
    print(count, "is less than 9")
    count += 1
else:
    print(count, 'is 9')

print('good bye')
print('\n')

# for loop

numbers = range(5)
for number in list(numbers):
    print(number)
print()

for letter in 'Pyhton':
    print('Current letter is:',letter)
print()

fruits = ['banana', 'grape', 'mango']
for fruit in fruits:
    print('Current fruit:',fruit)
print()

for index in range(len(fruits)):
    print('Current fruit is:',fruits[index])
else:
    print('else executed when for is finished')
print()

numbers = [1,9,3,2,7,5]
for num in numbers:
    if num%2 == 0:
        print('the list contains an even number')
        break
else:
    print('the list doesnot contain  even number')

# nested loop

for num1 in range(1,11):
    for num2 in range(1,11):
        res = num1 * num2
        print(res, end=' ')
    print()