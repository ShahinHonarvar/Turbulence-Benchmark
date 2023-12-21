
from itertools import permutations

def palindromes_between_indices(my_string):
    my_set = set()
    substring = my_string[1:10]
    perms = [''.join(p) for p in permutations(substring)]
    for perm in perms:
        if len(perm) >= 7 and perm.lower() == perm[::-1].lower():
            my_set.add(perm)
    return my_set
