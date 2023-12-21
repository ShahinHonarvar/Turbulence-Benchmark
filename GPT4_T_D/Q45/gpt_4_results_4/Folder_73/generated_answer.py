
from collections import Counter
from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[3:7].lower()
    letters = Counter(sub_str)
    candidates = set()
    
    for length in range(3, len(sub_str) + 1):
        for perm in permutations(sub_str, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                candidates.add(candidate)
                
    return candidates
