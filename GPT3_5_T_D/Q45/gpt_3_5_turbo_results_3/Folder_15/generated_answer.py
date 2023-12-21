
from itertools import permutations

def palindromes_between_indices(string):
    palindromes = set()
    letters = [letter.lower() for letter in string if letter.isalpha()]
    for perm in permutations(letters, 3):
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes
