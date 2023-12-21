
import itertools

def palindromes_between_indices(string):
    letters = [ch.lower() for ch in string[5:10] if ch.isalpha()]
    palindromes = set()
    for perm in itertools.permutations(letters):
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1] and len(palindrome) >= 4:
            palindromes.add(palindrome)
    return palindromes
