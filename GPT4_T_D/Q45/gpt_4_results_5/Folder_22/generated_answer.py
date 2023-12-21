
from itertools import permutations

def palindromes_between_indices(s):
    letters = s[5:7]
    palindromes = set()
    for i in range(3, len(letters) + 1):
        perms = [''.join(p) for p in permutations(letters, i)]
        for perm in perms:
            if perm.lower() == perm[::-1].lower():
                palindromes.add(perm)
    return palindromes
