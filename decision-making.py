#!/usr/bin/python3.8

# if statement
# Python programming language assumes any non-zero and non-null values as TRUE, and any zero or null values as FALSE value.

num1 = 100
if num1:
    print('variable num1 is true')
    print(num1)

num2 = 0
if num2:
    print('variable num2 is true')
    print(num2)

# if else statement

totalHarga = int(input("Masukan total harga:"))

if totalHarga>5000:
    diskon = totalHarga*0.10
    print("Diskon anda",diskon)
else:
    diskon = totalHarga*0.05
    print("Diskon anda",diskon)

print("Setelah didiskon: ",totalHarga-diskon)

# elif statement

totalPrice = int(input("Enter total price:"))

if totalPrice<5000:
    discount = totalPrice*0.02
    print("Your discount: ",discount)
elif totalPrice<10000:
    discount = totalPrice*0.05
    print("Your discount: ",discount)
else:
    discount = totalPrice*0.10
    print("Your discount: ",discount)
print("After discount: ", totalPrice-discount)

## nested if statement

angka = int(input("Masukan angka:"))

if angka%2 == 0:
    if angka%3 == 0:
        print(angka," bisa dibagi 2 dan 3")
    else:
        print(angka," bisa dibagi 2 tapi tidak bisa dibagi 3")
else:
    if angka%3 == 0:
        print(angka," bisa dibagi 3 tapi tidak bisa dibagi 2")
    else:
        print(angka," tidak bisa dibagi 2 dan 3")


## switch case statement

def week(angka):
    switcher={
        0:'Sunday',
        1:'Monday',
        2:'Tuesday',
        3:'Wednesday',
        4:'Thrusday',
        5:'Friday',
        6:'Saturday'
    }
    return switcher.get(angka,"Invalid day of week")

print(week(8))