
from itertools import permutations

def palindromes_between_indices(s):

    s = s.lower()[:6]
    all_pals = set()
    
    for p in permutations(s):
        current = "".join(p)
        if len(current) < 5:
            continue
        if current == current[::-1]:
            all_pals.add(current)
    
    return all_pals
