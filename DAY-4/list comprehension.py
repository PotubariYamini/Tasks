
# list [ expression if condition for item in sequence]

str1= [1,6,1,6,7,9,6,6,1,1,6,4,2,3]
for i in range (len(str1)): # range
  if str1 [i]==6:
     str1.pop(i)
     print(i)


