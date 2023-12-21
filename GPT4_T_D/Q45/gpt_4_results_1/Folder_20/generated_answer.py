
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:9].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(4, len(letters)+1):
        for perm in permutations(letters, i):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
