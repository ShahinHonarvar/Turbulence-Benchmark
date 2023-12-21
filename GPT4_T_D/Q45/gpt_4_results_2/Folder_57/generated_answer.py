
from itertools import permutations

def palindromes_between_indices(s):
    letters = s[2:6].lower()
    candidates = set()
    for p in permutations(letters):
        word = "".join(p)
        if word == word[::-1] and len(word) >= 5:
            candidates.add(word)
    return candidates
