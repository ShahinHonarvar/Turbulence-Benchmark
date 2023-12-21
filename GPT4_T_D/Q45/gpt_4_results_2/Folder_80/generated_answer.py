
from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:9]
    unique_chars = set(substring.lower())
    palindromes = set()
    for char_combination in permutations(unique_chars):
        candidate = ''.join(char_combination)
        if len(candidate) < 7:
            continue
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes
