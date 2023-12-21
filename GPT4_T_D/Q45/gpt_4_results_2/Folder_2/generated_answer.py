
from itertools import permutations

def palindromes_between_indices(s):
    part_str = sorted(s[1:6].lower())
    palindromes = set()
    
    for i in range(6, len(part_str)+1):
        for p in permutations(part_str, i):
            p_str = ''.join(p)
            if p_str == p_str[::-1]:
                palindromes.add(p_str)
    
    return palindromes
