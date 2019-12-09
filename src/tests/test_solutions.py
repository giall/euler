from unittest import main, TestCase
import solutions


class TestProblem10(TestCase):
    def test_should_return_correct_answer(self):
        self.assertEqual(solutions.summation_of_primes(), 142913828922)


class TestProblem16(TestCase):
    def test_should_return_correct_answer(self):
        self.assertEqual(solutions.power_digit_sum(), 1366)


class TestProblem20(TestCase):
    def test_should_return_correct_answer(self):
        self.assertEqual(solutions.factorial_digit_sum(), 648)


class TestProblem41(TestCase):
    def test_should_return_correct_answer(self):
        self.assertEqual(solutions.pandigital_prime(4), 4231)
        self.assertEqual(solutions.pandigital_prime(7), 7652413)


if __name__ == '__main__':
    main()
