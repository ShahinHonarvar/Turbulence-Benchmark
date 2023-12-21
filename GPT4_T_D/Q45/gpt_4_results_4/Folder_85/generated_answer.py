
from itertools import permutations

def palindromes_between_indices(s):

    sub_str = s[2:9].lower()

    pals = set()

    for i in range(7, len(sub_str) + 1):
        for permutation in permutations(sub_str, i):
            perm = ''.join(permutation)
            if perm == perm[::-1]:
                pals.add(perm)

    return pals
