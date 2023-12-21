
from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:10].lower()
    s = ''.join([i for i in s if i.isalpha()])
    pals = set()
    for i in range(5, len(s)+1):
        for perm in permutations(s, i):
            str_perm = ''.join(perm)
            if str_perm == str_perm[::-1]:
                pals.add(str_perm)
    return pals
