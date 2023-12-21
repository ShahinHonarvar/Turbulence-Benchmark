
from itertools import permutations

def palindromes_between_indices(s):
    s = s[7:9]
    possible_palindromes = set()
    for i in range(3, len(s) + 1):
        for perm in permutations(s, i):
            perm = "".join(perm).lower()
            if perm == perm[::-1]:
                possible_palindromes.add(perm)
    return possible_palindromes
