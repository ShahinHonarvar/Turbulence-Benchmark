
from itertools import permutations

def palindromes_between_indices(s):
    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    
    s = s[4:9]
    unique_combinations = set()
    for i in range(3, len(s) + 1):
        unique_combinations.update([''.join(p) for p in permutations(s, i)])

    return set(word for word in unique_combinations if is_palindrome(word))
