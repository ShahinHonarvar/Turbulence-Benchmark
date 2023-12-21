
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    sub_string = s[4:9]
    perm_list = [''.join(p) for p in permutations(sub_string)]
    palindromes = set()
    for perm in perm_list:
        if len(perm) < 5:
            continue
        if perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes
