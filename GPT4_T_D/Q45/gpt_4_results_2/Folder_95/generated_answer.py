
from itertools import permutations

def palindromes_between_indices(string):
    string = string[7:9].lower()
    perms_set = set()
    for perm in permutations(string):
        perm_string = "".join(perm)
        if perm_string == perm_string[::-1] and len(perm_string) >= 3:
            perms_set.add(perm_string)
    return perms_set
