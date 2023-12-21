
import itertools

def palindromes_between_indices(string):
    english_letters = [c.lower() for c in string if c.isalpha()]
    english_letters_set = set(english_letters)
    palindromes = set()
    for combination in itertools.permutations(english_letters_set, 6):
        palindrome = ''.join(combination)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes
