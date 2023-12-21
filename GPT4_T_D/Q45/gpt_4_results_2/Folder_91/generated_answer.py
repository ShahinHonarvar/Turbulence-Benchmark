
from itertools import permutations

def palindromes_between_indices(s):
    subs = s[2:7].lower()
    all_palindromes = set()
    for i in range(3, len(subs) + 1):
        for comb in permutations(subs, i):
            candidate = "".join(comb)
            if candidate == candidate[::-1]:
                all_palindromes.add(candidate)
    return all_palindromes
