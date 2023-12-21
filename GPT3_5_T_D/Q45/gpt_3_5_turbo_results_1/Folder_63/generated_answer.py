
import itertools

def palindromes_between_indices(string):
    string = string[:4].lower()
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for combination in itertools.permutations(letters):
        word = ''.join(combination)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes
