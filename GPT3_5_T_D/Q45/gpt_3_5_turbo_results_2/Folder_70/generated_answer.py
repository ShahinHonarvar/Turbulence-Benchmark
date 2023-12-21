
import itertools

def palindromes_between_indices(string):
    letters = [ch for ch in string[1:7] if ch.isalpha()]
    palindromes = set()
    for perm in itertools.permutations(letters):
        palindrome = ''.join(perm)
        if palindrome.lower() == palindrome.lower()[::-1] and len(palindrome) >= 4:
            palindromes.add(palindrome)
    return palindromes
