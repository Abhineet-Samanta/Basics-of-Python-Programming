class DemoClass:
    a=10
    def showValue(self):
        self.c=self.a *self.a
        print(self.c)
    def showValue1(self):
         print("Welcome")
    def showValue2(self,a,b):
         print(a+b)
    #constructor
    def __init__(self,a,b):
        print(a+b)
obj=DemoClass(8,8)
obj.showValue()
obj.showValue1()
obj.showValue2(8,8)