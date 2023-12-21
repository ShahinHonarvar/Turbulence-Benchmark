
from itertools import permutations

def palindromes_between_indices(string):
    string = string[7:10].lower()
    all_perms = [''.join(p) for p in permutations(string)]
    return set([x for x in all_perms if x == x[::-1] and len(x) >= 4])
