class A:
    def display(self):
        print("Welcome")
class B(A):
    def display1(self):
        print("Well")
obj=B()
obj.display()
obj.display1()