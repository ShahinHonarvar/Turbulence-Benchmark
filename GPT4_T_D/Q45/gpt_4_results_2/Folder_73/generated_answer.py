
from itertools import permutations

def palindromes_between_indices(s):
    letters = set(s[3:7].lower())
    palindromes = set()
    for l in letters:
        for p in permutations(letters):
            candidate = ''.join(p)
            if candidate == candidate[::-1] and len(candidate) >= 3:
                palindromes.add(candidate)
    return palindromes
