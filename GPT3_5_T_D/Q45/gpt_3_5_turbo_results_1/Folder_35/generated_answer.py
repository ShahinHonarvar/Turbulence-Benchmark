
import itertools

def palindromes_between_indices(string):
    letters = [letter.lower() for letter in string[2:5] if letter.isalpha()]
    
    palindromes = set()
    for perm in itertools.permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    
    return palindromes
