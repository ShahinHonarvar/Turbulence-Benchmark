
from itertools import permutations

def palindromes_between_indices(s):
    def is_palindrome(s):
        return s == s[::-1]
    
    s = s[0:7].lower()
    valid_chars = [c for c in s if c.isalpha()]
    possible_words = set([''.join(p) for p in permutations(valid_chars) if len(p) >= 4])
    palindromes = set([word for word in possible_words if is_palindrome(word)])

    return palindromes
