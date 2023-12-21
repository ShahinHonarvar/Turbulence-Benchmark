
import itertools

def palindromes_between_indices(string):
    english_letters = [ch for ch in string if ch.isalpha()]
    palindrome_set = set()

    for combination in itertools.permutations(english_letters, 4):
        palindrome = ''.join(combination).lower()
        if palindrome == palindrome[::-1]:
            palindrome_set.add(palindrome)

    return palindrome_set
