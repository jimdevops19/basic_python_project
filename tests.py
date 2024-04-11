# test.py
import unittest
from utils import calculate_pizza_cost

class TestPizzaCostCalculator(unittest.TestCase):
    def setUp(self):
        self.price_per_size = {'small': 5.99, 'medium': 7.99, 'large': 9.99}

    def test_small_pizza_cost(self):
        self.assertEqual(calculate_pizza_cost('small', self.price_per_size), 5.99)

    def test_medium_pizza_cost(self):
        self.assertEqual(calculate_pizza_cost('medium', self.price_per_size), 7.99)

    def test_large_pizza_cost(self):
        self.assertEqual(calculate_pizza_cost('large', self.price_per_size), 9.99)

    def test_invalid_pizza_size(self):
        self.assertEqual(calculate_pizza_cost('extra_large', self.price_per_size), 0.0)

if __name__ == '__main__':
    unittest.main()

