import random as r
l = ['Rock', 'Paper', 'Scissors']
Playerscore = 0
count = 0
while True:
    x = r.choice(l)  # move this inside loop so computer picks new each round
    y = input("Enter the choice (r/p/s) or 0 to quit: ")
    if y == 'p':
        if x == 'Rock':
            Playerscore += 1
            print("Your choice:", l[1], "Computer's choice:", l[0])
        elif x == 'Scissors':
            count += 1
            print("Your choice:", l[1], "Computer's choice:", l[2])
        elif x == 'Paper':
            print("Your choice:", l[1], "Computer's choice:", l[1])
    elif y == 'r':
        if x == 'Rock':
            print("Your choice:", l[0], "Computer's choice:", l[0])
        elif x == 'Scissors':
            Playerscore += 1
            print("Your choice:", l[0], "Computer's choice:", l[2])
        elif x == 'Paper':
            count += 1
            print("Your choice:", l[0], "Computer's choice:", l[1])
    elif y == 's':
        if x == 'Rock':
            count += 1
            print("Your choice:", l[2], "Computer's choice:", l[0])
        elif x == 'Scissors':
            print("Your choice:", l[2], "Computer's choice:", l[2])
        elif x == 'Paper':
            Playerscore += 1
            print("Your choice:", l[2], "Computer's choice:", l[1])
    elif y == '0':
        print("Your Score =", Playerscore)
        print("Computer Score =", count)
        break
    else:
        print("INVALID (Use r, p, s or 0 to quit)")



