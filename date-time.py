#!/usr/bin/python3.8

import time

print(time.time())
print(time.localtime())
print(time.asctime())

import calendar

print(calendar.month(2020,4))

print(time.strftime("%b",time.localtime()))
print(time.strftime("%B %u, %y",time.localtime()))