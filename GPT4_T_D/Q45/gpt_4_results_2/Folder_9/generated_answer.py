
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    s = s[0:7]
    palindromes = set()
    for i in range(7, len(s) + 1):
        for permutation in permutations(s, i):
            string = ''.join(permutation)
            if string == string[::-1]:
                palindromes.add(string)
    return palindromes
