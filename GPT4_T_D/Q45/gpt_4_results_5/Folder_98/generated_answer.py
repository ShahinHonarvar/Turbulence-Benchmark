
from itertools import permutations

def palindromes_between_indices(input_string):
    sub_string = input_string[3:6].lower()
    char_perms = [''.join(p) for p in permutations(sub_string) if len(p) >= 4]
    palindromes = set()

    for perm in char_perms:
        if perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes
