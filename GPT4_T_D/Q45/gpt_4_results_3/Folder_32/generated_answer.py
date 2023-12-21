
from itertools import permutations

def palindromes_between_indices(s):
    if len(s)<8:
        return set()
    s = s[1:8].lower()
    palindromes = set()
    for i in range(5, len(s) + 1):
        for p in permutations(s, i):
            p_str = ''.join(p)
            if p_str == p_str[::-1]:
                palindromes.add(p_str)
    return palindromes
