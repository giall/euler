from utils import is_pandigital, sieve_of_eratosthenes
from unittest import main, TestCase


class TestPandigital(TestCase):
    def test_should_return_true(self):
        self.assertTrue(is_pandigital(41235))

    def test_should_return_false(self):
        self.assertFalse(is_pandigital(41234))


class TestPrime(TestCase):
    primes = []

    def __init__(self, *args, **kwargs):
        super(TestPrime, self).__init__(*args, **kwargs)
        sieve = sieve_of_eratosthenes(100000)
        primes = [x for x in range(0, 100000) if sieve[x]]

    def test_should_return_true(self):
        self.assertTrue(9941 in self.primes)

    def test_should_return_true(self):
        self.assertFalse(9942 in self.primes)


if __name__ == '__main__':
    main()
