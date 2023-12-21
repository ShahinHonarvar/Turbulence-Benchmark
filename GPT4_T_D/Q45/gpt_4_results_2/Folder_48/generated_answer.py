
from itertools import permutations

def palindromes_between_indices(string):
    chars_between_indices = string[6:9]
    palindromes = set()

    for i in range(4, len(chars_between_indices) + 1):
        for p in permutations(chars_between_indices, i):
            word = ''.join(p).lower()
            if word == word[::-1]:
                palindromes.add(word)
                
    return palindromes
