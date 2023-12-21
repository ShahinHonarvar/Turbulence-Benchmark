
import itertools

def palindromes_between_indices(string):
    string = string.lower()
    english_letters = [char for char in string if char.isalpha()]
    palindromes = set()

    for length in range(4, 7):
        for combination in itertools.permutations(english_letters, length):
            palindrome = ''.join(combination)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)

    return palindromes
