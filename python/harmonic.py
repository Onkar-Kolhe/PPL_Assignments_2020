def harmonic(x):
    sum = 1 + (1/x)
    for i in range(2,x):
        if x % i == 0:
            sum += 1/i
            #print(i)
    #print(sum)
    return sum

def noofdivisors(y):
    no = 1
    for j in range(1,y):
        if y % j == 0:
            no += 1
    #print(no)
    return no

def harmonicpairs():
    count = 0
    k=0
    while count <=9:
        k += 1
        a = noofdivisors(k)
        b = harmonic(k)
        result = (a/b)
        if result % 1 == 0 and result % result == 0:
            count +=1
            print(k)
    return 0
#a=harmonic(8128)
#b=noofdivisors(8128)
harmonicpairs()
#print(b/a)