
from itertools import permutations

def palindromes_between_indices(string):
    sub_string = string[:6].lower()
    all_perms = [''.join(p) for p in permutations(sub_string)]
    palindromes_set = set()
    for perm in all_perms:
        if perm == perm[::-1] and len(perm) >= 6:
            palindromes_set.add(perm)
    return palindromes_set
