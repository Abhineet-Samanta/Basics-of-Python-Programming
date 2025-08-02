import random as r
x= r.randrange(1,101)
y=int (input("Enter the guessing number from 1 to 100 ="))
if y < 1 or y > 100:print("INVALID GUESS (1 to 100 only)")
elif y==x:print("the guessing number of computer =",x);print("the guessed number is  =", y);\
print("equal")
elif y<x:print("the guessing number of computer =",x);print("the guessed number is  =", y);\
print("guessed number is lower")
else:print("the guessing number of computer =",x);print("the guessed number is  =", y);\
print("guessed number is higher")
