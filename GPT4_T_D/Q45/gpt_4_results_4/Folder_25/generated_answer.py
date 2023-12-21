
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:5].lower()
    palindrome_set = set()
    for i in range(3, len(s) + 1):
        perms = [''.join(p) for p in permutations(s, i) if p == p[::-1]]
        palindrome_set.update(perms)
    return palindrome_set
