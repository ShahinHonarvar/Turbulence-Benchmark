
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[:5] if char.isalpha()]
    permutations = list(itertools.permutations(letters))
    palindromes = set()
    for perm in permutations:
        palindrome = "".join(perm)
        if palindrome == palindrome[::-1] and len(palindrome) >= 4:
            palindromes.add(palindrome)
    return palindromes
