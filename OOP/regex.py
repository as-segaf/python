#!/usr/bin/python3

## Regural Expression
# offers a set of functions that allows us to search a string for a match

## Metacharacters are characters with a special meaning

import re

txt = "I have 20 dollars"

x = re.findall("[a-j]",txt)     # find all lowercase characters alphabetically beetwen "a" and "j"
print(x)    # ['h', 'a', 'e', 'd', 'e']

x = re.findall("\d",txt)        # find all digit characters
print(x)    # ['2', '0']

x = re.findall("h..e",txt)      # search for a sequence that starts with "h", followed by two (any) characters, and an "e"
print(x)    # ['have']

x = re.findall("^have", txt)    # check if the string starts with have
if (x):
    print("the srting starts with 'have'")
else:
    print("the string doesn't start with 'have'")

x = re.findall("dollars$", txt) # check if the string ends with dollars
if x:
    print("the srting ends with 'dollars'")
else:
    print("the string doesn't end with 'dollars'")