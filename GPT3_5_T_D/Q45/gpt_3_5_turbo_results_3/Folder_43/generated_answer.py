
import itertools

def palindromes_between_indices(string):
    letters = [ch.lower() for ch in string if ch.isalpha()]
    letters_between_indices = letters[2:6]
    palindromes = set()
    for perm in itertools.permutations(letters_between_indices):
        palindrome = ''.join(perm)
        if palindrome.lower() == palindrome.lower()[::-1] and len(palindrome) >= 4:
            palindromes.add(palindrome)
    return palindromes
