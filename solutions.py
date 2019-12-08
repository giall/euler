from utils.utils import sieve_of_eratosthenes, is_pandigital
from functools import reduce


def summation_of_primes(n=1999999):
    """
    Summation of primes
    """
    sieve = sieve_of_eratosthenes(n)
    primes = [x for x in range(0, n) if sieve[x]]
    sum = reduce(lambda x, y: x + y, primes)
    return str(sum)


def pandigital_prime(n):
    """
    Pandigital prime
    """
    sieve = sieve_of_eratosthenes(n)
    primes = [x for x in range(0, n) if sieve[x]]
    pandigitals = [x for x in primes if is_pandigital(x)]
    return str(pandigitals[-1])
