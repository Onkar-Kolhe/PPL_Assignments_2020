# Guessing of Number from User
import random
z = random.randrange(1,1000)
a = input()
a = int(a)
while a != z :
    if a < z:
        print("Your number is smaller than choosed number")
        a = input()
        a = int(a)
    else :
        print("Your numbr is bigger than choosed number")
        a = input()
        a = int(a)
print("Your guess is correct")