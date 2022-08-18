
from re import A


class grandfather:
    def __init__(self,a):
       self.__y=a
       print(self.__y)
class father(grandfather):
    def displayf(self):
        print(self.__y)
class child1(father):
    def display1(self):
        print("child1 , self__y")
obj= child1(15)
obj.displayf()
obj.display1()

