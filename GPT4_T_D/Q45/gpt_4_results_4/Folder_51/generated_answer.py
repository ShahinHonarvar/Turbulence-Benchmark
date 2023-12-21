
from itertools import permutations

def palindromes_between_indices(string):
    substr = string[3:6].lower()
    palindrome_set = set()
    for permutation in permutations(substr):
        candidate = ''.join(permutation)
        if candidate == candidate[::-1] and len(candidate) >= 3:
            palindrome_set.add(candidate)
    return palindrome_set
