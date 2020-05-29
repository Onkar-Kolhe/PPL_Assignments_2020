def puzzle():
    bank1 = ["Goat","Tiger","Grass"]
    bank2 = []
    print("Pick the following choice number to cross the river along with man bank1 to bank2")
    a = input("1]Goat\t 2]Tiger\t 3]Grass\n")
    if a == '1':
        b = bank1.pop(int(a)-1)
        bank2.append(b)
        print("Pick the following choice number to cross the river along with man bank1 to bank2")
        a = input("1]Tiger\t 2]Grass\n")
        b = bank1.pop(int(a)-1)
        bank2.append(b)
        if "Goat" in bank2 and ("Tiger" in bank2 or "Grass" in bank2) :
            print("Goat was moved from bank2 to bank 1")
            c = bank2.pop(0)
            bank1.append(c)
            if b == 'Tiger':
                print("Pick the following choice number to cross the river along with man bank1 to bank2")
                a = input("1]Grass\t 2]Goat\n")
                if a != '2':
                    c = bank1.pop(int(a)-1)
                    bank2.append(c)
                    c = bank1.pop(0)
                    bank2.append(c)
                else :
                    print("Wrong choice")
                    c = bank1.pop(int(a)-1)
                    bank2.append(c)
            else :
                print("Pick the following choice number to cross the river along with man bank1 to bank2")
                a = input("1]Tiger \t 2]Goat\n")
                if a != '2':
                    c = bank1.pop(int(a)-1)
                    bank2.append(c)
                    c = bank1.pop(0)
                    bank2.append(c)
                else :
                    print("Wrong choice")
                    c = bank1.pop(int(a)-1)
                    bank2.append(c)
    else:
        print("Wrong choice")
        c = bank1.pop(int(a)-1)
        bank2.append(c)
    print("bank2",bank2)
    print("bank1",bank1)

puzzle()
