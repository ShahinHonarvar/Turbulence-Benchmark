
from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:10].lower()
    letters = [c for c in s if c.isalpha()]
    pals = set()
    for i in range(3, len(letters)+1):
        for perm in permutations(letters, i):
            perm = "".join(perm)
            if perm == perm[::-1]:
                pals.add(perm)
    return pals
