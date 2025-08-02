from math import gcd
class Fraction:
    def __init__(self,n,d):
        if d == 0:
            raise ValueError("Denominator cannot be zero.")
        self.n=n
        self.d=d
        self.simplify()
    def __str__(self):
        return "{}/{}".format(self.n,self.d)
    def __add__(self,other):
        temp_num=self.n*other.d +other.n * self.d
        temp_den=self.d*other.d
        return "{}/{}".format(temp_num, temp_den)
    def __sub__(self,other):
        temp_num=self.n*other.d -other.n * self.d
        temp_den=self.d*other.d
        return "{}/{}".format(temp_num, temp_den)
    def __mul__(self,other):
        temp_num=self.n*other.n
        temp_den=self.d*other.d
        return "{}/{}".format(temp_num, temp_den)
    def __truediv__(self, other):
        temp_num=self.n*other.d
        temp_den=self.d*other.n
        return "{}/{}".format(temp_num, temp_den)

    def simplify(self):
        common = gcd(self.n, self.d)
        self.n //= common
        self.d //= common
        if self.d < 0:
            self.n = -self.n
            self.d = -self.d
x=Fraction(5,6)
y=Fraction(10 ,6)
print(x)
print(y)
print(x+y)
print(x-y)
print(x*y)
print(x/y)





