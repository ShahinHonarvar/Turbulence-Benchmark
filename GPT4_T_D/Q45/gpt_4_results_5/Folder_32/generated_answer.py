
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:8].lower()
    s = ''.join(e for e in s if e.isalnum())
    palindromes = set()
    for length in range(5, len(s) + 1):
        for combo in permutations(s, length):
            string = ''.join(combo)
            if string == string[::-1]:
                palindromes.add(string)
    return palindromes
