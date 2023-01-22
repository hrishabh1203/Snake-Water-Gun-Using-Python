from operator import truediv
import random
def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 'S':
        if you == 'W':
            return False
        elif you == 'G':
            return True
        elif comp == 'W':
            if you == 'G':
                return False
            elif you == 'S':
                return True
    elif comp == 'G':
        if you == 'S':
            return False
        elif you == 'W':
            return True

randno = random.randint(1,3)
if randno == 1:
    comp = 'S'
elif randno == 2:
    comp = 'W'
elif randno == 3:
    comp = 'G'

you = input("Computer turn: Snake(S), Water(W) or Gun(G)?\n")
a = gameWin(comp, you)
print(f"Computer choose {comp}")
print(f"You choose {you}")

if a == None:
    print("The game is a tie")
elif a:
    print("You Win")
else:
    print("You loose")
