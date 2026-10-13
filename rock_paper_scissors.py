import random
print("Enter number corresponding to your sign: 1- Scissors, 2- Rock, 3- Paper")
w=0
r=0
while r<5:
    a=int(input("Enter your sign: "))
    if a not in [1,2,3]:
        print("Invalid value")
        continue
    r+=1
    c= random.choice([1, 2, 3])
    if (a==1 and c==3) or (a==2 and c==1) or (a==3 and c==2):
        print("Computer chose", c)
        print("Player Wins")
        w+=1
    elif (a==1 and c==2) or (a==2 and c==3) or (a==3 and c==1):
        print("Computer chose", c)
        print("Computer Wins")
    else:
        print("Match is a draw")
print("Total player wins is", w)