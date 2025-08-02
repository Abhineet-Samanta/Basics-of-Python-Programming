class Ws:
    def displayinfo(self):
        print("ABHI")
class IIP(Ws):
    def displayinfo(self):
        super().displayinfo()
        print("ABHINEET")
obj=IIP()
obj.displayinfo()