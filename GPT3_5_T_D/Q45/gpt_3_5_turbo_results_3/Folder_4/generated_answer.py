
import itertools

def palindromes_between_indices(string):
    letters = [char for char in string if char.isalpha()]
    palindromes = set()
    for perm in itertools.permutations(letters, 7):
        if ''.join(perm).lower() == ''.join(perm).lower()[::-1]:
            palindromes.add(''.join(perm).lower())
    return palindromes
