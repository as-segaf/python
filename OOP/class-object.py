#!/usr/bin/python3

class employee:
    'common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):   # read about 'self' in w3schools.com, it's easier to understand 
        self.nama = name
        self.gaji = salary
        employee.empCount += 1

    def displayCount(tes):
        print("Total employee:", tes.empCount)

    def displayEmployee(var):
        print('name:',var.nama, ', salary:', var.gaji)

emp1 = employee('bambang', 10000)   # This would create first object of employee class
emp2 = employee('agus', 20000)      # This would create second object of employee class

print(emp1.empCount)
print(emp1.gaji)
print(emp1.nama)
emp1.displayCount()
emp2.displayEmployee()

emp1.gaji = 5000    # Modify 'gaji' attribute
emp1.umur = 20      # Add 'umur' attribute
del emp1.gaji       # Delete 'gaji' attribute in emp1

hasattr(emp1, 'salary')         # Returns true if 'salary' attribute exists
getattr(emp1, 'salary')         # Returns value of 'salary' attribute
setattr(emp1, 'salary', 7000)   # Set attribute 'salary' at 7000
delattr(emp1, 'salary')         # Delete attribute 'salary'
