
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string if char.isalpha()]
    palindromes = set()
    for permutation in itertools.permutations(letters, 7):
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes
