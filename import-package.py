#!/usr/bin/python3

## you must put the package in the python path
## alternatively, you can append the path to sys.path

import sys
import phone

print(sys.path)
print()

## do this once
# sys.path.append(r'/var/www/html/backend/python')

print(sys.path)
print()


phone.pots()
phone.isdn()
phone.g3()
print()

## to remove the path from sys.path

sys.path.remove(r'/var/www/html/backend/python')
print(sys.path)

## stuck at here, removed successfully
## but when you run this file again, there is no errors appear
## and the path appears again in sys.path
 