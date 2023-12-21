
from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:9].lower()
    pals = set()
    for length in range(5, len(s) + 1):
        for perm in permutations(s, length):
            temp_str = ''.join(perm)
            if temp_str == temp_str[::-1]:
                pals.add(temp_str)
    return pals
