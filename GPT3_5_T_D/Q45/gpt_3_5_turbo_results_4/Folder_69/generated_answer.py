
import itertools

def palindromes_between_indices(string):
    english_letters = [char for char in string.lower() if char.isalpha()]
    if len(english_letters) < 4:
        return set()

    palindromes = set()
    for combination in itertools.permutations(english_letters[:4], 4):
        palindrome = "".join(combination)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)

    return palindromes
