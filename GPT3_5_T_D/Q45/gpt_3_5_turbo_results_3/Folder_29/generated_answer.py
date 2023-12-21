
import itertools

def palindromes_between_indices(s):
    english_letters = [c for c in s if c.isalpha()]
    english_letters = english_letters[2:10] if len(english_letters) >= 10 else []
    english_letters = [c.lower() for c in english_letters]

    palindromes = set()
    for p in itertools.permutations(english_letters, len(english_letters)):
        palindrome = ''.join(p)
        if palindrome == palindrome[::-1] and len(palindrome) >= 6:
            palindromes.add(palindrome)
    
    return palindromes
