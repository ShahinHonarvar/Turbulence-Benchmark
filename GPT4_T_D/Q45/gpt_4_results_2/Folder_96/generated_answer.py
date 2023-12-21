
from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:9].lower()
    palindromes = set()
    for i in range(6, len(s) + 1):
        for perm in permutations(s, i):
            string = ''.join(perm)
            if string == string[::-1]:
                palindromes.add(string)
    return palindromes
