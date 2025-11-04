def checkYear (n):
    if not n % 4 == 0:
        return False
    if n %100 == 0 and not n %400 == 0:
        return False
    return True