
from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:10].lower()
    result = set()
    for i in range(3, len(s) + 1):
        for p in permutations(s, i):
            p = ''.join(p)
            if p == p[::-1]:
                result.add(p)
    return result
