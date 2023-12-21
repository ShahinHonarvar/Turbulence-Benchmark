
from itertools import permutations

def palindromes_between_indices(string):
    str_range = string[0:7].lower()
    palindromes_set = set()

    for i in range(7, len(str_range) + 1):
        for perm in permutations(str_range, i):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes_set.add(perm_str)

    return palindromes_set
