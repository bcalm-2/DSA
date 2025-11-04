def sumOfDigits(self, n):
    digits = [int(digit) for digit in str(n)]
    sum = 0
    for digit in digits:
        sum = sum + digit
    return sum