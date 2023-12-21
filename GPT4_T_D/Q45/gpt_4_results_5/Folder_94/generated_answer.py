
from itertools import permutations

def palindromes_between_indices(string):
    substr = string[3:5]
    lower_substr = substr.lower()
    perms_set = set()
    for i in range(3, len(lower_substr)+1):
        perms_set.update("".join(p) for p in permutations(lower_substr,i) if "".join(p) == "".join(p)[::-1])
    return perms_set
