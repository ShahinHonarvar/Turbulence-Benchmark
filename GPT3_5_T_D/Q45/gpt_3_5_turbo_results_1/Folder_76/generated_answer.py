
import itertools

def palindromes_between_indices(string):
    palindromes = set()
    letters = ''.join(filter(str.isalpha, string[1:5])).lower()
    for perm in itertools.permutations(letters):
        palindrome = ''.join(perm).lower()
        if palindrome == palindrome[::-1] and len(palindrome) >= 4:
            palindromes.add(palindrome)
    return palindromes
