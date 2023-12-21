
import itertools

def palindromes_between_indices(string):
    letters = [letter.lower() for letter in string[1:8] if letter.isalpha()]
    palindromes = set()
    
    for word in itertools.permutations(letters, len(letters)):
        word = ''.join(word)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)

    return palindromes
