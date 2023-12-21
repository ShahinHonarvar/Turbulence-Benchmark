
from itertools import permutations

def palindromes_between_indices(string):
    string = string[5:10].lower()
    palindromes = set()
    for perm in permutations(string):
        s = ''.join(perm)
        if len(s) >= 5 and s == s[::-1]:
            palindromes.add(s)
    return palindromes
