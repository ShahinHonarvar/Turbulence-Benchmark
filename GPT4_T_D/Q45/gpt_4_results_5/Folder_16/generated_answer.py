
from itertools import permutations

def palindromes_between_indices(string):
    string = string.lower()
    string = string[6:10]
    unique_palindromes = set()
    for i in range(5, len(string)+1):
        perms = [''.join(p) for p in permutations(string, i)]
        for perm in perms:
            if perm == perm[::-1]:
                unique_palindromes.add(perm)
    return unique_palindromes
