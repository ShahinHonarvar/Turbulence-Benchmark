
from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:5] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for perm in permutations(letters):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes
