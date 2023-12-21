
from itertools import permutations

def palindromes_between_indices(str):
    letters = str[5:8].lower()
    letter_combos = [''.join(p) for p in permutations(letters) if len(p) >= 3]
    palindromes = set([combo for combo in letter_combos if combo == combo[::-1]])
    return palindromes
