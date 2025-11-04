def isPrime(self, n):
    if n == 1 or n ==0:
        return False
    for i in range(2, math.floor(n/2)):
        if n % i == 0:
            return False
    return True