import unittest
from Fraction import Fraction


class TestFraction(unittest.TestCase):
    f1 = Fraction(5, 6)
    f2 = Fraction(1, 2)

    def test_sub(self):
        self.assertEqual(self.f1 - self.f2, Fraction(1, 3))

    def test_add(self):
        self.assertEqual(self.f1 + self.f2, Fraction(4, 3))

    def test_equal(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 4)
        self.assertEqual(f1 == f2, True)

    def test_mul(self):
        self.assertEqual(self.f1 * self.f2, Fraction(5, 12))

    def test_div(self):
        self.assertEqual(self.f1 // self.f2, Fraction(5, 3))

    def test_ne(self):
        self.assertEqual(self.f1 != self.f2, True)

    def test_lt(self):
        self.assertEqual(self.f1 < self.f2, False)

    def test_le(self):
        self.assertEqual(self.f1 <= self.f2, False)

    def test_gt(self):
        self.assertEqual(self.f1 > self.f2, True)

    def test_ge(self):
        self.assertEqual(self.f1 >= self.f2, True)


