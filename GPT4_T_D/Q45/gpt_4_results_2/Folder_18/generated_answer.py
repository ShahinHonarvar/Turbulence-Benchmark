
from itertools import permutations

def palindromes_between_indices(string):
    substring = string[1:7].lower()
    palindromes_set = set()
    substring_length = len(substring)
    for i in range(3, substring_length + 1):
        perms = permutations(substring, i)
        for perm in perms:
            perm_str = "".join(perm)
            if perm_str == perm_str[::-1]:
                palindromes_set.add(perm_str)
    return palindromes_set
