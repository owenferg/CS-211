'''Owen Ferguson CS 211 Lab07 2-21-24'''

def total_sum(l: list[int]) -> int:
    '''Returns the sum of all elements in "l", a list of integers'''
    return sum(l)

def apply(f, l: list[int]) -> list:
    '''Returns a list created by apply f to every element in l'''
    result = []
    for elem in l:
        result.append(f(elem))

    return result

def square(l: list[int]) -> list[int]:
    '''Returns a similar list to l where every element in l is squared'''
    return apply(lambda x: x**2, l)
    
def magnitude(vector: list[int]) -> float:
    '''Returns magnitude of vector'''
    return total_sum(square(vector))**0.5 # **0.5 is taking square root

dispatch_table = {1: total_sum, 2: square, 3: magnitude}

class FunctionDispatcher:
    def __init__(self, d):
        '''d is a dictionary of functions'''
        self.d = d

    def process_command(self, key, l: list[int]):
        '''
        Uses keys to call appropriate fucnction on the array of integers
        and returns the result
        key: key indicating the command to execute
        l: list of integers
        '''
        return self.d[key](l)
    
# TESTS
fd = FunctionDispatcher(dispatch_table)
g = [1, 2, 3] # dispatch table keys
for i in g:
    print(fd.process_command(i, [3, 4]))
# prints:
# 7
# [9, 16]
# 5.0