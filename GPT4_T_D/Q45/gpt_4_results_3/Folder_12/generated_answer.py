
from itertools import permutations

def palindromes_between_indices(s):
    substr = s[3:9].lower()
    palSet = set()
    for i in range(4, len(substr)+1):
        for perm in permutations(substr, i):
            term = ''.join(perm)
            if term == term[::-1]:
                palSet.add(term)
    return palSet
