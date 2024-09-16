from unittest import TestCase
from math import sqrt
from statistics import average, variance, stdev


class StatisticsTest(TestCase):
    """Unit tests for average, variance, and stdev functions."""

    def test_variance_typical_values(self):
        """Test variance of typical values"""
        self.assertEqual(0.0, variance([10.0, 10.0, 10.0, 10.0, 10.0]))
        self.assertEqual(2.0, variance([1, 2, 3, 4, 5]))
        self.assertEqual(8.0, variance([10, 2, 8, 4, 6]))

    def test_variance_non_integers(self):
        """Test variance should work with decimal values"""
        # variance([x,y,z]) == variance([x+d,y+d,z+d]) for any d
        self.assertEqual(0.0, variance([5.0]))
        self.assertEqual(4.0, variance([0.0, 4.0]))
        # variance([0,4,4,8]) == 8
        self.assertEqual(8.0, variance([0.0, 4.0, 4.0, 8.0]))

    def test_stdev(self):
        """Test standard deviation should work with a single
         value and more than one value"""
        # standard deviation of a single value should be zero
        self.assertEqual(0.0, stdev([10.0]))
        # simple test
        self.assertEqual(2.0, stdev([1, 5]))
        # variance([0, 0.5, 1, 1.5, 2.0]) is 0.5
        self.assertEqual(sqrt(0.5), stdev([0, 0.5, 1, 1.5, 2]))

    def test_average(self):
        """Test the average function."""
        self.assertEqual(0.0, average([0.0]))
        self.assertEqual(5.0, average([5, 5, 5, 5, 5]))
        self.assertEqual(3.0, average([1, 2, 3, 4, 5]))

    def test_average_with_empty_list(self):
        """Test average with an empty list."""
        with self.assertRaises(ValueError):
            average([])

    def test_variance_with_empty_list(self):
        """Test variance with an empty list."""
        with self.assertRaises(ValueError):
            variance([])

    def test_stdev_with_empty_list(self):
        """Test standard deviation with an empty list."""
        with self.assertRaises(ValueError):
            stdev([])

    def test_average_with_non_empty_list(self):
        """Test average with a non-empty list."""
        self.assertEqual(8.0, average([8, 9, 7]))

    def test_variance_with_non_empty_list(self):
        """Test variance with a non-empty list."""
        self.assertAlmostEqual(variance([8, 9, 7]), 0.6666666666666666)

    def test_stdev_with_non_empty_list(self):
        """Test standard deviation with a non-empty list."""
        self.assertAlmostEqual(stdev([8, 9, 7]), 0.816496580927726)


# if __name__ == '__main__':
#     import unittest
#     unittest.main(verbosity=1)
