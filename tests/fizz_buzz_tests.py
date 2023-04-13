import unittest
from src.fizz_buzz import *

class TestFizzBuzz(unittest.TestCase):

    def test_number_divisible_by_3(self):
        self.assertEqual("fizz", fizz(3, 3))

    def test_number_divisible_by_5(self):
        self.assertEqual("buzz", buzz(5, 5))

    def test_number_divisible_by_3_and_5(self):
        self.assertEqual("fizzbuzz", fizz_buzz(15, 15))

    def test_number_returns_a_string (self):
        self.assertEqual ("7", fizz_buzz_number_to_string(7, 7))


