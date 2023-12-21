
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:7].lower()
    palindromes_set = set()
    letters_permutations = [''.join(p) for p in permutations(s)]
    for p in letters_permutations:
        if len(p) >= 7 and p == p[::-1]:
            palindromes_set.add(p)
    return palindromes_set
