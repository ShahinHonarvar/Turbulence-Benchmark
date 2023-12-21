
from itertools import permutations

def palindromes_between_indices(s):
    substr = list(s[5 : 10].lower())
    palindrome_set = set()

    for i in range(4, len(substr) + 1):
        for p in permutations(substr, i):
            if p == p[::-1]:
                palindrome_set.add(''.join(p))
                
    return palindrome_set
