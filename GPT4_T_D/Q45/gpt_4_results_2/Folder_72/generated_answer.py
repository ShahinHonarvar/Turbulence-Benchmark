
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:8].lower()
    p_set = set()
    for l in range(6, len(s) + 1):
        for subset in permutations(s, l):
            subset = ''.join(subset)
            if subset == subset[::-1]:
                p_set.add(subset)
    return p_set
