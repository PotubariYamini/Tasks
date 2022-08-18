
from calendar import c


class vani: # parameter
    def __init__(self,a,b,c,d): # functions
        self.abc=c
        self.ac=b
        self.ab=a
        self.ad=d
    def display (self):
        print(self.abc,self.ac,self.ab,self.ad)
        
obj=vani(30,23,9.8,'chandu')
obj.display()
