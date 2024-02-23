# Prime Numbers within Range: Use a function and a loop to print all prime numbers between 1 and 50.


def isPrime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def printPrimeInRange(minValue, maxValue):
    for i in range(minValue, maxValue + 1):
        if isPrime(i):
            print(i)


printPrimeInRange(1, 15)
