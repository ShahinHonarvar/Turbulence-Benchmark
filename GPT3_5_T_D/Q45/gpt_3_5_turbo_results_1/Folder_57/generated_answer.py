
import itertools

def palindromes_between_indices(string):
    english_letters = [char.lower() for char in string if char.isalpha()]
    palindromes = set()

    for combination in itertools.permutations(english_letters, 4):
        palindrome = ''.join(combination)
        if palindrome == palindrome[::-1] and len(palindrome) >= 5:
            palindromes.add(palindrome)

    return palindromes
