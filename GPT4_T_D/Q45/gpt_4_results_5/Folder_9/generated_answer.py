
from itertools import permutations

def palindromes_between_indices(string):
    string = string[0:7].lower()
    # create unique permutations
    perms = set(permutations(string))
    # filter, creating strings and checking for palindromes
    palindromes = set([''.join(p) for p in perms if ''.join(p) == ''.join(p)[::-1] and len(p) >= 7])
    return palindromes
