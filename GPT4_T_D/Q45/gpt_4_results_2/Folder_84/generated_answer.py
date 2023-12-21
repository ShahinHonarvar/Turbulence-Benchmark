
from itertools import permutations

def palindromes_between_indices(str):
    sub_str = str[4:10].lower()
    palindromes = set()
    for i in range(3, len(sub_str)+1):
        perms = list(permutations(sub_str, i))
        perms = list(set([''.join(p) for p in perms]))
        for p in perms:
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes
