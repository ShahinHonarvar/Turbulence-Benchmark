
from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:10].lower()
    palindromes = set()
    permuts = [''.join(p) for p in permutations(s)]

    for p in permuts:
        if p[::-1] == p:
            if len(p) >= 5:
                palindromes.add(p)

    return palindromes
