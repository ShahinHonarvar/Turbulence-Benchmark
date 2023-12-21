
from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:10].lower()
    palindromes = set()
    for i in range(len(s) - 4):
        for j in range(i + 5, len(s) + 1):
            substrings = [''.join(p) for p in permutations(s[i:j])]
            palindromes.update([string for string in substrings if string == string[::-1]])
    return palindromes
