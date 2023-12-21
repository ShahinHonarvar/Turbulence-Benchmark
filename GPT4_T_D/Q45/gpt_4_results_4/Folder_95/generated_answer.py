
from itertools import permutations

def palindromes_between_indices(s):
    s = s[7:9].lower()
    possible_palindromes = set()
    for i in range(3, len(s)+1):
        perms = permutations(s, i)
        for p in perms:
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                possible_palindromes.add(candidate)
    return possible_palindromes
