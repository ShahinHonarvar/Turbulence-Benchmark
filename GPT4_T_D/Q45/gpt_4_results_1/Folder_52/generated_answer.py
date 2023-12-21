
from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:8].lower()
    palindromes = set()

    for i in range(6, len(s) + 1):
        for p in permutations(s, i):
            p = "".join(p)
            if p == p[::-1]:
                palindromes.add(p)

    return palindromes
