
from itertools import permutations

def palindromes_between_indices(s):
    substr = s[4:8].lower()
    palindromes = set()
    for length in range(5, len(substr) + 1):
        for p in permutations(substr, length):
            s = ''.join(p)
            if s == s[::-1]:
                palindromes.add(s)
    return palindromes
