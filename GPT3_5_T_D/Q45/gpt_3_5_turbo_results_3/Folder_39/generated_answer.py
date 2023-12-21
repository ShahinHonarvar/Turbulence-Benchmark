
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[2:6] if c.isalpha()]
    palindromes = set()
    for permutation in itertools.permutations(letters):
        palindrome = "".join(permutation)
        if palindrome.lower() == palindrome.lower()[::-1] and len(palindrome) >= 3:
            palindromes.add(palindrome.lower())
    return palindromes
