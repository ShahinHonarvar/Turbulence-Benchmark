
from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[2:7].lower()
    s_set = set()
    for i in range(5, len(s) + 1):
        for subset in permutations(s, i):
            substring = "".join(subset)
            if is_palindrome(substring):
                s_set.add(substring)
    return s_set
