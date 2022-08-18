# map(function,iterables)
# iterables (list,tuple)
def calculateAddition (m):
    return m**3
numbers=(1,2,3,4,5)
results= map(calculateAddition,numbers)
print(list(results))
