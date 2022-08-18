
# fliter (function,sequence)
kirshna= (12,22,35,24) # tuple
def myFunc (x): # function definition
    if x<20:
        return False
    else:
        return True
adults= filter(myFunc,kirshna)
# (function (true or false) ,sequence)
print(adults)
