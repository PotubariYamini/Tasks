

# tell() method
# open the file in read mode
file=open('FILE HANDLING/file.txt',mode='r+') # open(location)
# peint the position of handle
content=file.read()
v=str(content)
print(v)
p=v.split(v)
print(p)
p.insert(2,'arha')
print(file.tell())
#closing file
file.close()
file=open('FILE HANDLING/file.txt',mode='w') # open(location)
for i in p:
    file.writelines([i])
