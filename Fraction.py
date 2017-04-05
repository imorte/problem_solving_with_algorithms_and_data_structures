class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __ne__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum != secondnum

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __floordiv__(self, otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __lt__(self, otherfraction):
        newden = self.den * otherfraction.den

        return (newden // self.den) * self.num < (newden // otherfraction.den) * otherfraction.num

    def __le__(self, otherfraction):
        newden = self.den * otherfraction.den

        return (newden // self.den) * self.num <= (newden // otherfraction.den) * otherfraction.num

    def __gt__(self, otherfraction):
        newden = self.den * otherfraction.den

        return (newden // self.den) * self.num > (newden // otherfraction.den) * otherfraction.num

    def __ge__(self, otherfraction):
        newden = self.den * otherfraction.den

        return (newden // self.den) * self.num >= (newden // otherfraction.den) * otherfraction.num


def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n

f1 = Fraction(5, 6)
f2 = Fraction(1, 2)

print(f1 + f2)
