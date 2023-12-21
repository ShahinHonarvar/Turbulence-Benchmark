
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:6].lower()
    result = set()
    for i in range(3, len(s)+1):
        for j in permutations(s, i):
            x = ''.join(j)
            if x == x[::-1]:
                result.add(x)
    return result
