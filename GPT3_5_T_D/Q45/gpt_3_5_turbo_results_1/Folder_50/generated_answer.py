
import itertools

def palindromes_between_indices(string):
    english_letters = [ch for ch in string if ch.isalpha()]
    english_letters = english_letters[4:9]
    palindromes = set()
    for permutation in itertools.permutations(english_letters):
        palindrome = ''.join(permutation).lower()
        if palindrome == palindrome[::-1] and len(palindrome) >= 5:
            palindromes.add(palindrome)
    return palindromes
