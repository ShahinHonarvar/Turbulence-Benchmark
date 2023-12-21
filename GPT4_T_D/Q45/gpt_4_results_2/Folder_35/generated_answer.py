
from itertools import permutations

def palindromes_between_indices(input_string):
    letters = input_string[2:5].lower()
    perm = [''.join(p) for p in permutations(letters) if len(p) >= 4]
    return set(word for word in perm if word == word[::-1])
