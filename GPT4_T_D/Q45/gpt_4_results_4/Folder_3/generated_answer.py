
from itertools import permutations

def palindromes_between_indices(string):
    letters = string[7:10].lower()
    palindromes = set()
    for comb in permutations(letters):
        word = ''.join(comb)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes
