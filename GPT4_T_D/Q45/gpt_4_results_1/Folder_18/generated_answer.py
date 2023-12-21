
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:7].lower()
    palindromes = set()
    for i in range(3, len(s)+1):
        for p in permutations(s, i):
            p_str = ''.join(p)
            if p_str == p_str[::-1]:
                palindromes.add(p_str)
    return palindromes
