
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string if char.isalpha()]
    palindromes = set()
    for combination in itertools.permutations(letters, 7):
        palindrome = ''.join(combination)
        if palindrome.lower() == palindrome.lower()[::-1]:
            palindromes.add(palindrome)
    return palindromes
