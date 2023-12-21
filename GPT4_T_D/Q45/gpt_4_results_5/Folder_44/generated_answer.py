
from itertools import permutations

def palindromes_between_indices(s):
    palindrome_set = set()
    relevent_chars = s[2:8].lower()
    for r in range(3, len(relevent_chars)+1):
        for perm in permutations(relevent_chars, r):
            string = ''.join(perm)
            if string == string[::-1]:
                palindrome_set.add(string)
    return palindrome_set
