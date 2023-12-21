
import itertools

def palindromes_between_indices(string):
    string = string[3:7]
    letters = [char.lower() for char in string if char.isalpha()]
    palindromes = set()
    for combination in itertools.permutations(letters):
        word = ''.join(combination)
        if len(word) >= 3 and word.lower() == word.lower()[::-1]:
            palindromes.add(word)
    return palindromes if palindromes else set()
