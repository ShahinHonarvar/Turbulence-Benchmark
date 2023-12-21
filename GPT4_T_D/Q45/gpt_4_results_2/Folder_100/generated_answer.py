
from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:6].lower()
    distinct_chars = ''.join(set(s))
    
    palindromes = set()
    for l in range(6, len(distinct_chars)+1):
        for perm in permutations(distinct_chars, l):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
                
    return palindromes
