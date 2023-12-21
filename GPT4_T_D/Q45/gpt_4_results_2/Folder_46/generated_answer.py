
from itertools import permutations

def palindromes_between_indices(s):
    s=s[4:10]
    palindromes=set() 
    for p in permutations(s, 6):
        p=''.join(p).lower()
        if p==p[::-1]: 
            palindromes.add(p)
    return palindromes
