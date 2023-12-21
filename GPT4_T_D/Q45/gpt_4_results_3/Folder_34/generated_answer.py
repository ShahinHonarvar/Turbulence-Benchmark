
from itertools import permutations

def palindromes_between_indices(s):
    substr = s[5:8].lower()
    palindromes_set = set()
    possible_combinations = [''.join(p) for p in permutations(substr)]
    for word in possible_combinations:
        if len(word) >= 4 and word == word[::-1]:
            palindromes_set.add(word)
    return palindromes_set
