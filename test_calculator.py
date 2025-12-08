
# file: test_calculator.py
import unittest
from calculator import add

class TestCalculator(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-2, 3), 1)
    # test comment
    def test_add_two_numbers(self):
        self.assertEqual(add(4, 4), 8)

if __name__ == '__main__':
    unittest.main()
