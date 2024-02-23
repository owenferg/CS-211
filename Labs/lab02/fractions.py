'''Owen Ferguson
Lab 02: Fractions 1-19-2024'''

def gcd(a, b) -> int:
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

class Fraction():
    
    def __init__(self, num, den):
        assert den > 0 and num >= 0, 'Denominator cannot be 0 and Numerator cannot be negative'

        self.num = num
        self.den = den

        self.simplify()

    def __str__(self) -> str:
        return f'{self.num}/{self.den}'
    
    def __repr__(self):
        return f'Fraction({self.num}, {self.den})'
    
    def __mul__(self, other: 'Fraction') -> 'Fraction':
        new_num = self.num * other.num
        new_den = self.den * other.num

        result = Fraction(new_num, new_den)
        result.simplify()
        return result
    
    def __add__(self, other: 'Fraction') -> 'Fraction':
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den

        result = Fraction(new_num, new_den)
        result.simplify()
        return result
    
    def simplify(self):
        new_gcd = gcd(self.num, self.den)
        self.num //= new_gcd
        self.den //= new_gcd
