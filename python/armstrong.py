def armstrong():
    d = input()
    e = input()
    d = int(d)
    e = int(e)
    if d < e:
        for i in range(d,e):
            z = noofplaces(i)
            c = i
            sum = 0
            while c > 0 :
                r = c % 10
                f = pow(r,z)
                sum = sum + f
                c = c // 10
            if  sum == i:
                print(sum)
    return 0

def noofplaces(x):
    j = 0
    while x > 0:
        x = x // 10
        j += 1
    return j 

armstrong()

