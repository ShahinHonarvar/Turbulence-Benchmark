
from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:9].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for i in range(7, len(s) + 1):
        for p in permutations(s, i):
            possible_palindrome = ''.join(p)
            if possible_palindrome == possible_palindrome[::-1]:
                palindromes.add(possible_palindrome)
    return palindromes
