
import itertools

def palindromes_between_indices(string):
    letters = [letter.lower() for letter in string[7:10] if letter.isalpha()]    
    palindromes = set()
    for permut in itertools.permutations(letters, len(letters)):
        word = ''.join(permut)
        if len(word) >= 4 and word == word[::-1]:
            palindromes.add(word)
    return palindromes
