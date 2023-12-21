
from itertools import permutations

def palindromes_between_indices(in_string):
    in_string = in_string[0:8].lower()
    palindromes = set()
    for i in range(4, len(in_string) + 1):
        perms = permutations(in_string, i)
        for p in perms:
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes
