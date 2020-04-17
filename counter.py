#!/usr/bin/python3.8

from collections import Counter

c = Counter({'a':3,'b':2,'c':4})
print(c)
c = Counter('hello')
print(c)
# c = Counter(a=2,b=3,c=5)
# print(c)

# update counter doesn't replace the existing

c.update('world')
print(c)

# access count

print(c['l'])
print(c['a'])

for i in c.elements():
    print(f"{i}: {c[i]}")