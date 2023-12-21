
from itertools import permutations

def palindromes_between_indices(str_arg):
    str_subset = str_arg[4:10].lower()
    unique_permutations = set([''.join(p) for p in permutations(str_subset) if len(p)>=3])

    palindromes = set()
    for perm in unique_permutations:
        if perm == perm[::-1]:
            palindromes.add(perm)

    return palindromes
