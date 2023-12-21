
import itertools

def palindromes_between_indices(string):
    english_letters = [c for c in string.lower() if c.isalpha()]
    permutations = set(itertools.permutations(english_letters, 7))
    palindromes = set()
    for permutation in permutations:
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes
