
import itertools

def palindromes_between_indices(string):
    chars = [c for c in string[3:6] if c.isalpha()]
    palindromes = set()
    for permutation in itertools.permutations(chars):
        palindrome = ''.join(permutation).lower()
        if palindrome == palindrome[::-1] and len(palindrome) >= 3:
            palindromes.add(palindrome)
    return palindromes
