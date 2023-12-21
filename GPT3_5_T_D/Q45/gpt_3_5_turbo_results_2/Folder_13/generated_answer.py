
import itertools

def palindromes_between_indices(string):
    indices = range(3, 10)
    english_letters = [ch for ch in string if ch.isalpha()]

    perms = set(itertools.permutations(english_letters, len(indices)))
    palindromes = set()

    for perm in perms:
        palindrome = ''.join(perm).lower()
        if palindrome == palindrome[::-1] and len(palindrome) >= 5:
            palindromes.add(palindrome)

    return palindromes
