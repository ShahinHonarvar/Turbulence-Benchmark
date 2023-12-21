
from itertools import permutations

def palindromes_between_indices(str):
    str = str[5:10].lower()
    palindromes = set()
    for comb in permutations(str):
        comb_str = ''.join(comb)
        if comb_str == comb_str[::-1] and len(comb_str) >= 6:
            palindromes.add(comb_str)
    return palindromes
