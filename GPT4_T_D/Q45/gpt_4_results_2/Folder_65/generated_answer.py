
from collections import Counter
from itertools import permutations
def palindromes_between_indices(string):
    string_to_consider = string.lower()[:7]
    palindromes = set()
    letters = [ch for ch in string_to_consider if ch.isalpha()]
    for p in permutations(letters):
        possible_word = ''.join(p).lower()
        if len(possible_word) < 5 or possible_word != possible_word[::-1]:
            continue
        palindromes.add(''.join(p))
    return palindromes
