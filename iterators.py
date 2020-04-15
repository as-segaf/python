#!/usr/bin/python3.8

## Iterators
## is an object that can be iterated upon
## lists, tuples, dictionaries, sets are all iterable objects

myTuple = ("apple","banana","cherry")   # Tuple is iterable
myIt = iter(myTuple)                    # myIt is a tuple iterator, check the type

print(next(myIt))
print(next(myIt))
print(next(myIt))

myStr = "mango"                         # String is iterable
myIt = iter(myStr)                      # myIt is a string iterator, check the type

print(next(myIt))
print(next(myIt))
print(next(myIt))
print(next(myIt))
print(next(myIt))

## The for loop actually creates an iterator object and executes the next() method for each loop
for i in myTuple:
    print(i)

for i in myStr:
    print(i)


class myNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myClass = myNumber()
myIter = iter(myClass) 

for i in myIter:
    print(i)