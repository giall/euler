from utils.utils import sieve_of_eratosthenes, is_pandigital
from functools import reduce


def summation_of_primes(n=1999999):
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    """
    sieve = sieve_of_eratosthenes(n)
    primes = [x for x in range(0, n) if sieve[x]]
    sum = reduce(lambda x, y: x + y, primes)
    return sum

def power_digit_sum(n=2 ** 1000):
  """
  2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

  What is the sum of the digits of the number 2 ** 1000?
  """
  characters = list(str(n))
  digits = list(map(lambda x: int(x), characters))
  sum = reduce(lambda x, y: x + y, digits)
  return sum

def pandigital_prime(n):
    """
    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
    For example, 2143 is a 4-digit pandigital and is also prime.

    What is the largest n-digit pandigital prime that exists?
    """
    max = 10 ** n
    sieve = sieve_of_eratosthenes(max)
    primes = [x for x in range(0, max) if sieve[x]]
    pandigitals = [x for x in primes if is_pandigital(x)]
    return pandigitals[-1]
