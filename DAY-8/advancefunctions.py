# lambda argumnet: expression
# A= lambda x,y,z:x-y-z # parameters
# calling function
# print(A(3,8,False))

# lambda argument: expression
a=[14,16,17,20,34] # list
b=[] # empty list
for i in a: # a=[14,16,17,20,34]
    s= lambda d : d+2
    b.append(s(i))
    print(b)




