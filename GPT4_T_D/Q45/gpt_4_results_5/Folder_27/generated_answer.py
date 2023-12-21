
from itertools import permutations

def palindromes_between_indices(string):
    letters = string[2:9].lower()
    palindromes = set()
    for i in range(6, len(letters) + 1):
        for perm in permutations(letters, i):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
