def makeATriangle(n):
    for value in range(1, n+1):
        i = 0
        while(i < value):
            print(value, end=" ")
            i += 1
        print()


makeATriangle(9)
