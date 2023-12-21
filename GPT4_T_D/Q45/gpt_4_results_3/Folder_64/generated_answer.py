
from itertools import permutations

def palindromes_between_indices(s):
    letters = list(s[4:10].lower())
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for p in permutations(letters, i):
            p_str = ''.join(p)
            if p_str == p_str[::-1]:
                palindromes.add(p_str)
    return palindromes
