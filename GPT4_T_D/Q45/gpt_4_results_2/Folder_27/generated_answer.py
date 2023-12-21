
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:9].lower()
    palindromes = set()
    
    for i in range(6, len(s)+1):
        for perm in permutations(s, i):
            temp = ''.join(perm)
            if temp == temp[::-1]:
                palindromes.add(temp)
    return palindromes
