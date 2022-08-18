
def simplegeneratorFun():
    yield 1
    yield 2
    yield 3
## x is a generator object
y= simplegeneratorFun()
# iterating over the generator using next
print(y.__next__()) # in python ,__next__
print(y.__next__()) # in python ,__next__
print(y.__next__()) # in python ,__next__

