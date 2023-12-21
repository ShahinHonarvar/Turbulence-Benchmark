
from itertools import permutations

def palindromes_between_indices(s):
    possible_chars = s[1:8].lower()
    possible_combinations = [''.join(p) for p in permutations(possible_chars)]
    possible_combinations = [pc for pc in possible_combinations if len(pc) >= 6]
    palindromes = set()
    for comb in possible_combinations:
        if comb == comb[::-1]:
            palindromes.add(comb)
    return palindromes
