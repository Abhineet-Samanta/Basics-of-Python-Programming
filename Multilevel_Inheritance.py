class A:
    def display(self):
        print("Welcome")
class B:
    def display1(self):
        print("Well")
class C(B,A):
    def display2(self):
        print("We")
obj=C()
obj.display()
obj.display1()
obj.display2()