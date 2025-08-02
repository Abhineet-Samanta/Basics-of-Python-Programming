class Area:
    def area(self,x=None,y=None):
        if x!=None and y!=None:print(x*y)
        elif x!=None:print(x*x)
        else:print("nothing")
obj1=Area()
obj1.area()
obj1.area(8)
obj1.area(8,8)