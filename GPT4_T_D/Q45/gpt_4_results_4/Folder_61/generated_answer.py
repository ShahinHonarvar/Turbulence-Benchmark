
from collections import Counter
from itertools import permutations

def palindromes_between_indices(string):
    string = string[:8].lower()
    result = set()

    for perm in permutations(string):
        s = ''.join(perm)
        if s == s[::-1] and len(s) >= 7:
            result.add(s)

    return result
