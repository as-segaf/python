#!/usr/bin/python3

## Special sequences
## is a "\" followed by a character and has a special meaning

import re

txt = "The rain in Spain"
x = re.findall("\AThe",txt)         # check if the string starts with "The"
print(x)

x = re.findall(r"\bSp",txt)         # check if "Sp" is at the beginning of a word
print(x)

x = re.findall(r"in\b",txt)         # check if "in" is at the end of a word
print(x)

x = re.findall(r"\Bin",txt)         # check if "in" is present but NOT at the beginning of a word    
print(x)

x = re.findall(r"in\B",txt)         # check if "in" is present but NOT at the end of a word
print(x)

string = "I have 20 dollars"
x = re.findall("\d",string)         # return every digit character
print(x)

x = re.findall("\D",string)         # return every no-digit character
print(x)

x = re.findall("\s",string)         # return every white-space character
print(x)

x = re.findall("\S",string)         # return every NON white-space character
print(x)

x = re.findall("\w",string)         # return every word character (characters from a-Z, digits from 0-9, and the underscore "_" character)
print(x)

x = re.findall("\W",string)         # return every NON word character (characters NOT between a-Z. Like "!"."?",white-space, etc)
print(x)

x = re.findall("dollars\Z",string)  # check if the text ends with "Spain"
print(x)