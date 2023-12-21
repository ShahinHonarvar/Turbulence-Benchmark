
from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:7].lower()
    letters = [char for char in s if char.isalpha()]
    perms = []
    for i in range(3, len(letters) + 1):
        perms += [''.join(p) for p in permutations(letters, i)]
    return set(word for word in perms if word == word[::-1])
