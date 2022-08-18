
class Methodoverri:
    def display(self):
        print("this is a parent class")
class child (Methodoverri):
    def display(self):
        print("this is child class")
        super().display()
obj=child()
obj.display()


