import unittest
import simple_calculator

class TestSimpleCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(simple_calculator.add(2,2),4)
        self.assertEqual(simple_calculator.add(2,-2),0)

    def test_subtract(self):
        self.assertEqual(simple_calculator.subtract(2,2),0)    

if __name__ == "__main__":
    unittest.main()        