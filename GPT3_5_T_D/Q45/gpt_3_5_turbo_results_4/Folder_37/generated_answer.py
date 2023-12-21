
import itertools

def palindromes_between_indices(string):
    letters = [char for char in string[1:5] if char.isalpha()]
    palindromes = set()
    for perm in itertools.permutations(letters):
        palindrome = ''.join(perm).lower()
        if palindrome == palindrome[::-1] and len(palindrome) >= 5:
            palindromes.add(palindrome)
    return palindromes
