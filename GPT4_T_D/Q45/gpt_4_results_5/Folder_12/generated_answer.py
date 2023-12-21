
from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:9].lower()
    palindromes = set()
    possible_combinations = set("".join(p) for p in permutations(s))

    for word in possible_combinations:
        if len(word) >= 4 and word == word[::-1]:
            palindromes.add(word)

    return palindromes
