
import itertools

def palindromes_between_indices(string):
    letters = []
    for char in string[3:8]:
        if char.isalpha():
            letters.append(char.lower())
    palindromes = set()
    for perm in itertools.permutations(letters):
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1] and len(palindrome) >= 6:
            palindromes.add(palindrome)
    return palindromes
