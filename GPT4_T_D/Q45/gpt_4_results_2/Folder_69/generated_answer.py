
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    chars = s[0:4]
    words = set()
    for i in range(4, len(chars) + 1):
        for perm in permutations(chars, i):
            word = ''.join(perm)
            if word == word[::-1]:
                words.add(word)
    return words
