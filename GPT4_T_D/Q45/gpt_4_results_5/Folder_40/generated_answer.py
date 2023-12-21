
from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:10].lower()
    palindromes = set()
    for i in range(7, len(s)+1):
        for perm in permutations(s, i):
            s_perm = "".join(perm)
            if s_perm == s_perm[::-1]:
                palindromes.add(s_perm)
    return palindromes
