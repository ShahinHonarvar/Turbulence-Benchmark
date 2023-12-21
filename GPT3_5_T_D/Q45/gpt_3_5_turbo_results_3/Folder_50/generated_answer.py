
import itertools


def palindromes_between_indices(string):
    letters = [ch for ch in string[4:9] if ch.isalpha()]
    palindromes = set()
    
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation).lower()
        if palindrome == palindrome[::-1] and len(palindrome) >= 5:
            palindromes.add(palindrome)
    
    return palindromes
