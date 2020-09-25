import random

def whowin(flag,comp,you):
    if you==comp:
        flag=2
    elif you=='r' and comp=='s':
        flag=1
    elif comp=='r' and you=='s':
        flag=0
    elif you=='p' and comp=='r':
        flag=1
    elif comp=='p' and you=='r':
        flag=0
    elif you=='s' and comp=='p':
        flag=1
    elif comp=='p' and you=='s':
        flag=0

    return flag

#MAIN FUNCTION

print("\n***WELCOME TO THE GAME***")
print("**ROCK PAPER SCISSOR**")
ch=True

while(ch):
    comp = random.randint(1, 100)
    if comp > 0 and comp <= 33:
        comp = 'r'
    elif comp > 33 and comp <= 66:
        comp = 'p'
    else:
        comp = 's'

    print("\nPress r for Rock\nPress p for Paper\nPress s for Scissor\n")
    you = input()
    flag = 0

    a = whowin(flag, comp, you)

    if a == 1:
        print("\nCONGRATULATIONS!! You WON !!")
    elif a == 0:
        print("\nYou Lose! Better Luck Next Time")
    else:
        print("GAME DRAW!!")

    print("Computer Chose : ", comp)

    print("\nPress y to play again\nPress q to exit ")
    ch=input()
    if ch=='y':
        ch=True
    else:
        print("\nGAME OVER !!")
        ch=False


