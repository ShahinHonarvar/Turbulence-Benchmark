
from itertools import permutations

def palindromes_between_indices(s):
    substr = s[4:6].lower()
    chars = [c for c in substr if c.isalpha()]
    all_pals = set()
    
    for i in range(3, len(chars) + 1):
        for perm in permutations(chars, i):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                all_pals.add(candidate)
                
    return all_pals
