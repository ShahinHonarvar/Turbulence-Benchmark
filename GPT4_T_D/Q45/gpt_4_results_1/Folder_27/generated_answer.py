
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:9].lower()
    palindromes = set()
    for length in range(6, len(s) + 1):
        for perm in permutations(s, length):
            string = ''.join(perm)
            if string == string[::-1]:
                palindromes.add(string)
    return palindromes
