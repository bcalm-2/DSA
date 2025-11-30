def printNos(n):
    if n == 0:
        return
    else:
        print(n,end=" ")
        printNos(n - 1)