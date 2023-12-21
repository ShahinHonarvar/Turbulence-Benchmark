
import itertools

def palindromes_between_indices(string):
    substring = string[8:10]
    letters = [c.lower() for c in substring if c.isalpha()]
    possible_pals = set(''.join(p) for p in itertools.permutations(letters) if len(p)>=3)
    return {p for p in possible_pals if p == p[::-1]}
