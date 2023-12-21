
import itertools

def palindromes_between_indices(s):
    letters = [letter.lower() for letter in s if letter.isalpha()]
    palindromes = set()
    for arrangement in itertools.permutations(letters, 9):
        palindrome = ''.join(arrangement)
        if palindrome == palindrome[::-1] and len(palindrome) >= 7:
            palindromes.add(palindrome)
    return palindromes
