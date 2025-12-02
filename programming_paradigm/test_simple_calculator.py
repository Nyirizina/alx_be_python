import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_add(self):
        self.assertEqual(self.calc.add(2, 6), 8)
        self.assertEqual(self.calc.add(-3, -4), -7)
        self.assertEqual(self.calc.add(-5, 6), 1)
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(8, 8), 0)
        self.assertEqual(self.calc.subtract(-3, -8), 5)
        self.assertEqual(self.calc.subtract(-5, 6), -11)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 6), 12)
        self.assertEqual(self.calc.multiply(-3, -4), 12)
        self.assertEqual(self.calc.multiply(-5, 6), -30)
    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 4), 2)
        self.assertEqual(self.calc.divide(-12, -4), 3)
        self.assertEqual(self.calc.divide(-15, 3), -5)
        self.assertIsNone(self.calc.divide(5, 0))
if __name__ == '__main__':
    unittest.main()