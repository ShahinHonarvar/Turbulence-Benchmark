
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[1:4] if char.isalpha()]
    if len(letters) < 4:
        return set()

    palindromes = set()
    for combination in itertools.permutations(letters):
        palindrome = ''.join(combination) + ''.join(reversed(combination))
        palindromes.add(palindrome.lower())

    return palindromes
