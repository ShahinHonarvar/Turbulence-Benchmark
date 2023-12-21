
from itertools import permutations

def palindromes_between_indices(s):
    lower_case_s = s.lower()
    sub_string = lower_case_s[0:5]
    return_set = set()
    unique_perms = set([''.join(p) for p in permutations(sub_string)])

    for word in unique_perms:
        if len(word) >= 3 and word == word[::-1]:
            return_set.add(word)

    return return_set
