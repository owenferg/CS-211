'''Owen Ferguson
CS 211: Anagrams 1-24-2024'''

"""A bag of letters for finding anagrams.
Associates a cardinality (count) with each character
in the bag.
"""

def normalize(phrase: str) -> list[str]:
    """Normalize word or phrase to the
    sequence of letters we will try to match, discarding
    anything else, such as blanks and apostrophes.
    Return as a list of individual letters.
    """
    return [char.lower() for char in phrase if char.isalpha()]

class LetterBag:
    """A bag (also known as a multiset) is
    a map from keys to non-negative integers.
    A LetterBag is a bag of single character
    strings.
    """
    def __init__(self, word=''):
        '''Create a LetterBag'''
        self.word = word.strip()
        normal = normalize(self.word)
        self.length = len(normal) # counts letters only
        self.letters = {}
        for char in normal:
            if char in self.letters:
                self.letters[char] += 1
            else:
                self.letters[char] = 1

    def __len__(self):
        return self.length

    def __str__(self):
        return self.word

    def __repr__(self):
        counts = [f"{ch}:{n}" for ch, n in self.letters.items() if n > 0]
        return f'LetterBag({self.word}/[{", ".join(counts)}])'

    def contains(self, other: 'LetterBag') -> bool:
        '''Determine whether enough of each letter in other LetterBag are contained in this LetterBag'''
        for char, ct in other.letters.items():
            if char not in self.letters or self.letters[char] < ct:
                return False
        return True
    
    def copy(self) -> 'LetterBag':
        '''Make a copy before mutating'''
        copy_ = LetterBag()
        copy_.word = self.word
        copy_.letters = self.letters.copy()  # Copied to avoid aliasing
        copy_.length = self.length
        return copy_

    def take(self, other: 'LetterBag') -> 'LetterBag':
        """Return a LetterBag after removing
        the letters in other.  Raises exception
        if any letters are not present.
        """
        for char in other.letters:
            assert char in self.letters
        
        bag = self.copy()
        for char, ct in other.letters.items():
            if bag.letters[char] >= ct:
                bag.letters[char] -= ct
                if bag.letters[char] == 0:
                    bag.letters.pop(char)

        new_word = ''
        for char, ct in bag.letters.items():
            new_word += char * ct
        
        bag.word = new_word
        bag.length = len(bag.word)

        return bag