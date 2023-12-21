
from itertools import permutations

def palindromes_between_indices(s):
    palindrome_set = set()
    s = s.lower()
    perm_list = [''.join(p) for p in permutations(s[1:3])]
    for word in perm_list:
        if len(word) >= 3 and word == word[::-1]:
            palindrome_set.add(word)
    return palindrome_set
