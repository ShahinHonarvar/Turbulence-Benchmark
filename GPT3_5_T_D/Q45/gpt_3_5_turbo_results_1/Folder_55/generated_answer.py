
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[:3] if char.isalpha()]
    palindromes = set()
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1] and len(palindrome) >= 3:
            palindromes.add(palindrome)
    return palindromes
