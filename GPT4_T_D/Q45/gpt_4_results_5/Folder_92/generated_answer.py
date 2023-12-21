
from itertools import permutations

def palindromes_between_indices(str):
    str = str[4:8].lower()
    str = str.replace(' ', '')
    palindromes = set()

    for p in permutations(str):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)

    return palindromes
