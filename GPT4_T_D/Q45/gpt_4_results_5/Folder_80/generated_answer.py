
from itertools import permutations

def palindromes_between_indices(string):
    def is_palindrome(word):
        return word == word[::-1]

    letters = string[3:9].lower()
    perms = [''.join(p) for p in permutations(letters) if len(''.join(p)) >= 7]
    palindromes = set([word for word in perms if is_palindrome(word)])

    return palindromes
