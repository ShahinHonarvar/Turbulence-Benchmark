
from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:6].lower()
    palindromes = set()

    for i in range(5, len(s) + 1):
        perm = permutations(s, i)
        for p in list(perm):
            string = ''.join(p)
            if string == string[::-1]:
                palindromes.add(string)
    
    return palindromes
