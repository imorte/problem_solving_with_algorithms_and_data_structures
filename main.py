class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newdem = self.den * otherfraction.den
        return Fraction(newnum, newdem)


f1 = Fraction(1, 4)
f2 = Fraction(1, 2)


print(f1 + f2)
