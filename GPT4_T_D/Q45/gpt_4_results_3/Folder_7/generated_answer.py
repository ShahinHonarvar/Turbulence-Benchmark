
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:10].lower()
    s = ''.join(ch for ch in s if ch.isalpha()) # filter only English letters
    palindromes_set = set()
    for length in range(7, len(s) + 1):
        for perm in permutations(s, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes_set.add(candidate)
    return palindromes_set
