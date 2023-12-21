
from itertools import permutations

def palindromes_between_indices(s):
    chars = s[2:5].lower()
    palindromes = set()
    
    for i in range(3, len(chars)+1):
        for perm in permutations(chars, i):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
                
    return palindromes
