
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:7].lower()
    s = ''.join([char for char in s if char.isalpha()])
    unique_pals = set()
    for i in range(6, len(s)+1):
        perms = [''.join(p) for p in permutations(s, i)]
        for perm in perms:
            if perm == perm[::-1]:
                unique_pals.add(perm)
    return unique_pals
