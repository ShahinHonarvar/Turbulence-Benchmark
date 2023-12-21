
from itertools import permutations

def palindromes_between_indices(string):
    sub_str = string[3:8].lower()
    letters = [letter for letter in sub_str if letter.isalpha()]
    perms = [''.join(p) for p in permutations(letters) if len(p) >= 5]
    palindromes = set()
    for p in perms:
        if p == p[::-1]:
            palindromes.add(p)
    return palindromes
