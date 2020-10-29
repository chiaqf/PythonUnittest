import unittest
import main


class SimpleTest(unittest.TestCase):

    # Returns True or False.
    def test_sum(self):
        self.assertEqual(main.sum(5,3), 8)

    def test_subtract(self):
        self.assertEqual(main.subtract(5,3), 2)

    def test_multiply(self):
        self.assertEqual(main.multiply(3,5), 15)

    def test_divide(self):
        self.assertEqual(main.divide(4,5), 0.8)

    def test_hypothenuse(self):
        self.assertEqual(main.hypothenuse(3,4), 5)

if __name__ == '__main__':
    unittest.main()
