
from collections import Counter
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    available_letters = Counter(s[3:10])
    available_palindromes = set()

    for length in range(3, len(available_letters) + 1):
        for substring in permutations(available_letters, length):
            palindrome = ''.join(substring).lower()
            if palindrome == palindrome[::-1]:
                available_palindromes.add(palindrome)
                
    return available_palindromes
