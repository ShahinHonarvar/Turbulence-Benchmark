
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[:7] if char.isalpha()]
    palindromes = set()
    for perm in itertools.permutations(letters):
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1] and len(palindrome) >= 6:
            palindromes.add(palindrome)
    return palindromes
