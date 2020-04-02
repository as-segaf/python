#!/usr/bin/python3.8

## import
import module

module.say_hello("bambang")

## from...import

from module import print_str
print_str("bambang")
# say_hello("agus")       # NameError : name 'say_hello' is not defined

from module import *
say_hello("agus")
print_filename()

content = dir(module)
print(content)