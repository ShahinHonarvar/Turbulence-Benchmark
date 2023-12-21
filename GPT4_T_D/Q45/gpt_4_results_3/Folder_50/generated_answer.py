
from itertools import permutations

def palindromes_between_indices(s):
    letters = s[4:9].lower()
    palindromes = set()
    for length in range(5, len(letters)+1):
        perm = permutations(letters, length)
        for i in list(perm):
            palindrome_candidate = ''.join(i)
            if palindrome_candidate == palindrome_candidate[::-1]:
                palindromes.add(palindrome_candidate)
    return palindromes
