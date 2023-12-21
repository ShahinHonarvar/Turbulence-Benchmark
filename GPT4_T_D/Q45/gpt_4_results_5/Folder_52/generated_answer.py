
from itertools import permutations

def palindromes_between_indices(string):
    substring = string[:8]
    palindrome_set = set()
    perms = permutations(substring.lower(), 6)
    for perm in list(perms):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            palindrome_set.add(candidate)
    return palindrome_set
