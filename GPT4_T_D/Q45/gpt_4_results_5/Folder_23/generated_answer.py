
from collections import Counter
from itertools import permutations

def palindromes_between_indices(strng):
    def is_palindrome(s):
        return s == s[::-1]
        
    strng = strng.lower()
    strng = strng[0:7]
    letter_count = Counter(strng)
    palindromes = set()
    
    for perm_len in range(4, len(strng) + 1):
        for comb in permutations(strng, perm_len):
            comb_str = ''.join(comb)
            if is_palindrome(comb_str):
                palindromes.add(comb_str)
    return palindromes
