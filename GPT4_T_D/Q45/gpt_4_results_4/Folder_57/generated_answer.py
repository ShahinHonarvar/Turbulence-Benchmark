
from itertools import permutations

def palindromes_between_indices(s):
    palindromes = set()
    s = s[2:6].lower()
    for i in map(''.join, permutations(s)):
        if len(i) >= 5 and i == i[::-1]:
            palindromes.add(i)
    return palindromes
