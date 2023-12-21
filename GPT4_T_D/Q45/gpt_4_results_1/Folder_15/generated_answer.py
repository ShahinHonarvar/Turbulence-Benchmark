
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:3].lower()
    pals = set()
    for i in range(3, len(s)+1):
        for p in permutations(s, i):
            candidate = "".join(p)
            if candidate == candidate[::-1]:
                pals.add(candidate)
    return pals
