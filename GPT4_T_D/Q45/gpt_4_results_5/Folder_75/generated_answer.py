
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:5].lower()
    palindromes = set()
    for p in permutations(s):
        p = ''.join(p)
        if len(p) >= 3 and p == p[::-1]:
            palindromes.add(p)
    return palindromes
