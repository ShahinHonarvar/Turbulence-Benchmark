
from itertools import permutations

def palindromes_between_indices(s):
    substr = s[8:10].lower()
    substr_len = len(substr)
    palindrome_set = set()
    
    if substr_len >= 3:
        perms = set("".join(p) for p in permutations(substr))
        
        for perm in perms:
            if perm == perm[::-1]:
                palindrome_set.add(perm)
                
    return palindrome_set
