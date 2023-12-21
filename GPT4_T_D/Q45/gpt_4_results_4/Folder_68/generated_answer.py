
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:9].lower()
    palindromes = set()
    for i in range(4, len(s) + 1):
        perms = permutations(s, i)
        for perm in perms:
            string = ''.join(perm)
            if string == string[::-1]:
                palindromes.add(string)
    return palindromes
