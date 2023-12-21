
import itertools

def palindromes_between_indices(string):
    letters = [letter.lower() for letter in string[4:9] if letter.isalpha()]
    palindromes = set()
    for comb in itertools.permutations(letters):
        palindrome = ''.join(comb)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes
