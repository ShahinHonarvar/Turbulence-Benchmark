
import itertools

def palindromes_between_indices(string):
    letters = [letter.lower() for letter in string[1:8] if letter.isalpha()]
    palindromes = set()

    for combination in itertools.permutations(letters):
        palindrome = ''.join(combination)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)

    return palindromes
