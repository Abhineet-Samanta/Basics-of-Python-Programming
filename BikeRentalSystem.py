class bikeShop:
    def __init__(self, stock):
        self.stock = stock

    def displayBike(self):
        print("Total Bikes:", self.stock)

    def rentforbike(self, q):
        if q <= 0:
            print("Enter a value greater than zero.")
        elif q > self.stock:
            print("Enter a value less than or equal to current stock.")
        elif q <= self.stock:
            print("Total Price:", q * 100)
            self.stock -= q
            print("Bikes remaining after rent:", self.stock)
obj = bikeShop(100)          # Make sure this line is OUTSIDE the loop
while True:
    try:
        uc = int(input("\n1. Display Stock\n2. Rent a bike\n3. Exit\nEnter your choice: "))
    except ValueError:
        print("Please enter a number (1‑3).")
        continue
    if uc == 1:
        obj.displayBike()
    elif uc == 2:
        try:
            n = int(input("Enter quantity: "))
            obj.rentforbike(n)
        except ValueError:
            print("Please enter an integer quantity.")
    elif uc == 3:
        print("Thank you! Visit again.")
        break
    else:
        print("Invalid choice. Please try again.")