
# Dice Rolling Simulator
import random
x=random.randrange(1,7)
print(x)
while 1:
    z = input("For playing again please enter Y  or press 'ENTER' ")
    if z == 'y' or 'Y' :
        x=random.randrange(1,7)
        print(x)
    else :
        break;



