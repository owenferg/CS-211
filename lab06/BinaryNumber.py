'''Owen Ferguson Lab06 Binary Number 2-14-2024'''

class BinaryNumber():
    def __init__(self, bits: list[int]):
        '''bits is a list of integers where all ints are 1 or 0'''
        self.bits = bits

    def __or__(self, other: 'BinaryNumber') -> 'BinaryNumber':
        assert len(self.bits) == len(other.bits), f'Both numbers have to be the same length'
        new_bits = []
        for i in range(len(self.bits)):
            if self.bits[i] == 1 or other.bits[i] == 1:
                new_bits.append(1)
            else:
                new_bits.append(0)
        return BinaryNumber(new_bits)
    
    def __and__(self, other: 'BinaryNumber') -> 'BinaryNumber':
        assert len(self.bits) == len(other.bits), f'Both numbers have to be the same length'
        new_bits = []
        for i in range(len(self.bits)):
            if self.bits[i] == 0 or other.bits[i] == 0:
                new_bits.append(0)
            else:
                new_bits.append(1)
        return BinaryNumber(new_bits)
    
    def left_shift(self, n: int=1):
        '''n is amount shifted, changes object, default 1'''
        new_bits = self.bits
        for i in range(n):
            new_bits.append(0)
        self.bits = new_bits[n:]

    def right_shift(self, n: int=1):
        '''n is amount shifted, changes object, default 1'''
        new_bits = self.bits
        extra = []
        for i in range(n):
            extra.append(0)
        self.bits = extra + new_bits[:-n]

    def __str__(self):
        return f'{self.bits}'