
from itertools import permutations

def palindromes_between_indices(string):
    substring = string[1:9]
    palindromes_set = set()
    for i in range(7, len(substring)+1):
        for perm in permutations(substring, i):
            perm_str = "".join(perm).lower()
            if perm_str == perm_str[::-1]:
                palindromes_set.add(perm_str)
    return palindromes_set
