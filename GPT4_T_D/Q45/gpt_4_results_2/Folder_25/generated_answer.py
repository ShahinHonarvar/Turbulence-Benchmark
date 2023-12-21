
from itertools import permutations

def palindromes_between_indices(s):
    subs = s[1:5].lower()
    palindromes = set()
    for i in range(3, len(subs) + 1): 
        for p in permutations(subs, i):
            st = "".join(p)
            if st == st[::-1]: 
                palindromes.add(st)
    return palindromes
