
from itertools import permutations
def palindromes_between_indices(s):
    s = s[0:5].lower()
    p_set = set()
    for i in range(3, len(s)+1):
        for p in permutations(s, i):
            if "".join(p) == "".join(p)[::-1]:
                p_set.add("".join(p))
    return p_set
