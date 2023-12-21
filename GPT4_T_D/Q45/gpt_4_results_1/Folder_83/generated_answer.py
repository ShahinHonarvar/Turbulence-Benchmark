
from itertools import permutations

def palindromes_between_indices(text):
    text = text[2:10].lower()
    palindromes = set()
    for i in range(7, len(text) + 1):
        for perm in permutations(text, i):
            s = ''.join(perm)
            if s == s[::-1]:
                palindromes.add(s)
    return palindromes
