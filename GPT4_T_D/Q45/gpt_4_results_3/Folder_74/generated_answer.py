
from itertools import permutations 

def palindromes_between_indices(s):
    palindromes = set()
    letters = s[1:7].lower()
    for i in range(6, len(letters) + 1):
        for perm in permutations(letters, i):
            perm_str = "".join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes
