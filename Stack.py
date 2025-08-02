l=[]
while True:
    c=input("1-Push,2-Pop,3-Peek, 4-Display,5-Exit:-")
    if c=="1":
        n= input("Enter Value:-")
        l.append(n)
        print(l)
    elif c=="2":
        if len(l)==0:print("Empty Stack")
        else:
              p= l.pop()
              print(p)
              print(l)
    elif c=="3":
         if len(l)==0:print("Empty Stack")
         else:print(l[-1])
    elif c=="4":
          print(l)
    elif c=="5":break
    else:print("Invalid choice — enter 1‑5.")