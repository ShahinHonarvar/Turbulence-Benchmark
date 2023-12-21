
from itertools import permutations

def palindromes_between_indices(s):
    s = s[6:9]
    letters = [ch.lower() for ch in s if ch.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            p = ''.join(perm)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes
