"""Closed intervals of integers
Owen Ferguson, 2024-01-10, CIS 211
"""

class Interval:
    """An interval m..n represents the set of intervals at least m and at most n."""

    def __init__(self, low: int, high: int):
        """Interval(low,high) is the interval low..high"""
        assert low < high
        self.low = low
        self.high = high

    def contains(self, i: int) -> bool:
        """Integer i is within the closed interval"""
        if i in range(self.low, self.high + 1):
            return True
        return False

    def overlaps(self, other: "Interval") -> bool: 
        """i.overlaps(j) if i and j have some elements in common"""
        return self.high >= other.low and self.low <= other.high or other.high >= self.low and other.low <= self.high
    
    def __eq__(self, other: "Interval") -> bool:
        """Intervals are equal if they have the same low and high bounds"""
        return self.high == other.high and self.low == other.low
    
    def join(self, other: "Interval") -> "Interval":
        """Create a new Interval that contains the union of elements in self and other.
        Precondition: self and other must overlap.
        """
        assert(self.overlaps(other))

        new_low = min([self.low, other.low])
        new_high = max([self.high, self.low]) 

        return Interval(new_low, new_high)
