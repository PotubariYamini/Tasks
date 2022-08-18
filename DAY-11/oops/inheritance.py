class Father:
 def output(self):
     print("this father class")
class child1(Father):
 def outputchild1(self):
     print("this is child1 class")
class child2(Father):
    def outputchild2(self):
        print("this is child2 class")
i=child1()
h=child2()
i.output()
i.outputchild1()
h.output()
h.outputchild2()

    