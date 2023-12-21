
import itertools

def palindromes_between_indices(string):
    english_letters = [ch for ch in string if ch.isalpha()]
    possible_palindromes = set()
    for combo in itertools.permutations(english_letters, 2):
        palindrome = ''.join(combo[0] + combo[1])
        if palindrome.lower() == palindrome.lower()[::-1]:
            possible_palindromes.add(palindrome)
    return possible_palindromes if possible_palindromes else set()
