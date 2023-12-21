
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    s = s[3:10]
    palindromes = set()

    for p in permutations(s):
        p = ''.join(p)
        if p == p[::-1] and len(p) >= 7:
            palindromes.add(p)

    return palindromes
