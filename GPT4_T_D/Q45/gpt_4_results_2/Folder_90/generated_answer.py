
from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:6].lower()
    all_pals = set() 
    for length in range(4, len(s) + 1):
        for perm in permutations(s, length):
            to_check = ''.join(perm)
            if to_check == to_check[::-1]:
                all_pals.add(to_check)
    return all_pals
