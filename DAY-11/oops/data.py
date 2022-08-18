from abc import ABC,abstractmethod
class parent (ABC):
    @abstractmethod
    def done (self):
        pass
    @abstractmethod
    def ramesh(self):
        pass
class child(parent):
    def done(self,a):
        print("this is child class",a)
    def ramesh(self):
        print("this is another class")
obj=child()
obj.done(13)
obj.ramesh()

