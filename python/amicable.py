def sumofdivisor(z):
    sum = 1
    for i in range(2,z):
        if z % i == 0:
            sum += i
    return sum


def countofpairs(x):
    count = 0
    while count <= 9:
        y = sumofdivisor(x)
        if sumofdivisor(y) == x and x != y and x < y :
            count +=1
            print(y,x)
        x+=1
        
    return 0

print(countofpairs(220))