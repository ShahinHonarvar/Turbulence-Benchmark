
from itertools import permutations

def palindromes_between_indices(s):
    string_set = s[0:8].lower()
    perms = set()
    for i in range(4, len(string_set) + 1):
        perms |= set(''.join(chars) for chars in permutations(string_set, i))
    return set(perm for perm in perms if perm == perm[::-1])
