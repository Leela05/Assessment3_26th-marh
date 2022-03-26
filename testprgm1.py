import prgm1
import unittest

class check_armstromg_number(unittest.TestCase):
    def setUp(self):
        self.number1 = 371
        self.number2 = 12

    def tearDown(self):
        self.number1 = 0
        self.number2 = 0

    def test_armstrong(self):
        result = prgm1.armstrong(self.number1)
        self.assertEqual("Armstrong number", result)

    def test_not_armstrong(self):
        result = prgm1.armstrong(self.number2)
        self.assertEqual("Not an Armstrong number", result)

class checkDivisibleBy5(unittest.TestCase):
    def setUp(self):
        self.number1 = 5
        self.number2 = 9

    def tearDown(self):
        self.number1 = 0
        self.number2 = 0

    def test_divisible(self):
        result = prgm1.divisible_by_5(self.number1)
        self.assertTrue(result)

    def test_not_divisible(self):
        result = prgm1.divisible_by_5(self.number2)
        self.assertTrue(result)

class check_largest_of_3numbers(unittest.TestCase):
    def setUp(self):
        self.number1 = 5
        self.number2 = 10
        self.number3 = 15

    def tearDown(self):
        self.number1 = 0
        self.number2 = 0
        self.number3 = 0

    def test_largest_number(self):
        result = prgm1.Largest(self.number1, self.number2, self.number3)
        self.assertEqual(self.number3, result)


class check_even_odd(unittest.TestCase):
    def setUp(self):
        self.number1 = 2
        self.number2 = 3


    def tearDown(self):
        self.number1 = 0
        self.number2 = 0

    def test_case1(self):
        result = prgm1.even_or_odd(self.number1)
        self.assertEqual("even", result)

    def test_case2(self):
        result = prgm1.even_or_odd(self.number2)
        self.assertEqual("odd", result)

if __name__=="__main__":
    unittest.main()
