
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[2:7] if c.isalpha()]
    arrangements = set(''.join(arrangement) for arrangement in itertools.permutations(letters))
    palindromes = set(arrangement for arrangement in arrangements if arrangement == arrangement[::-1] and len(arrangement) >= 4)
    return palindromes
