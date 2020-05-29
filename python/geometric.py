def geometric():
    d = input("Enter the first term")
    e = input("Enter the ratio")
    d = float(d)
    e = float(e)

    for i in range (0,10):
        z = d*(pow(e,i))
        print(z)
    return 0

geometric()
    