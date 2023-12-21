
import itertools

def palindromes_between_indices(string):
    valid_chars = [ch for ch in string[4:10] if ch.isalpha()]
    palindromes = set()
    
    for perm in itertools.permutations(valid_chars, len(valid_chars)):
        palindrome = ''.join(perm)
        if len(palindrome) >= 7 and palindrome.lower() == palindrome.lower()[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
