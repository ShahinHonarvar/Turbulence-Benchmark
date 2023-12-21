
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[5:10] if char.isalpha()]
    palindromes = set()
    for char_list in itertools.permutations(letters):
        word = ''.join(char_list)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes
