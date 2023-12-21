
import itertools

def palindromes_between_indices(string):
    letters = [char for char in string[4:7] if char.isalpha()]
    palindromes = set()
    for combo in itertools.permutations(letters):
        word = ''.join(combo).lower()
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes
