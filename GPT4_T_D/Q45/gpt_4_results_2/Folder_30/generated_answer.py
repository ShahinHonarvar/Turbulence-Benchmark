
from itertools import permutations

def palindromes_between_indices(string):
    string = string[0:5].lower()
    string_permutations = [''.join(perm) for perm in permutations(string) if len(perm) >= 4]
    palindromes = {perm for perm in string_permutations if perm == perm[::-1]}
    return palindromes
