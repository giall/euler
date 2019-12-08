def is_pandigital(n):
    string = str(n)
    digits = []
    for i in range(0, len(string)):
        x = int(string[i])
        if x in digits:
            return False
        if x > len(string) or x == 0:
            return False
        digits.append(x)
    return True


def sieve_of_eratosthenes(n):
    primes = [True for i in range(n+1)]
    x = 2
    while (x * x <= n):
        if primes[x] == True:
            for i in range(x * 2, n + 1, x):
                primes[i] = False
        x += 1
    primes[0] = False
    primes[1] = False
    return primes
