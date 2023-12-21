
from itertools import permutations

def palindromes_between_indices(s):
    substr = s[0:7].lower()
    palin_set = set()
    
    for i in range(4, len(substr) + 1):
        for perm in permutations(substr, i):
            new_str = ''.join(list(perm))
            if new_str == new_str[::-1]:
                palin_set.add(new_str)
                
    return palin_set
