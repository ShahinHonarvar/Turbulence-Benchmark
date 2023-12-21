
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:8].lower()
    palindromes = set()
    for i in range(3, len(s)+1):
        perms = [''.join(p) for p in permutations(s, i)]
        for p in perms:
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes
