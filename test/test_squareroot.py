import unittest
import squareroot as sr


class test_square_root(unittest.TestCase):
    def test_square_root(self):
        """ Test the square root values against a reference for x >= 0."""
        self.assertEqual(sr.square_root(1), 1)
        self.assertEqual(sr.square_root(0), 0)
        self.assertEqual(sr.square_root(9), 3)

    def test_values(self):
        """Make sure value errors are recognized for square_root."""
        self.assertRaises(ValueError, sr.square_root, -7)
