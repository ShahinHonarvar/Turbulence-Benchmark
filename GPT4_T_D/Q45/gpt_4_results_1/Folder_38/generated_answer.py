
from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:9].lower()
    english_alphabets = [c for c in s if c.isalpha()]

    perms = set()

    for i in range(5, len(english_alphabets) + 1):
        for p in permutations(english_alphabets, i):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                perms.add(candidate)

    return perms
