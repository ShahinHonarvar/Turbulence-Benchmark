
from itertools import permutations

def palindromes_between_indices(str):
    str = str[2:6].lower()
    length = len(str)
    palindromes = set()
    if length < 5:
        return palindromes
    for i in range(5, length+1):
        perms = [''.join(p) for p in permutations(str, i)]
        for perm in perms:
            if perm == perm[::-1]:
                palindromes.add(perm)
    return palindromes
