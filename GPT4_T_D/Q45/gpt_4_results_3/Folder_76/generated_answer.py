
from itertools import permutations

def palindromes_between_indices(string):
    sub_str = string[1:5].lower()
    possible_combinations = set()

    for perm in permutations(sub_str):
        perm_str = ''.join(perm)
        if len(perm_str) >= 4 and perm_str == perm_str[::-1]:
            possible_combinations.add(perm_str)

    return possible_combinations
