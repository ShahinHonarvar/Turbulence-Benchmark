
import itertools

def palindromes_between_indices(string):
    string = string[:6].lower()
    english_letters = [char.lower() for char in string if char.isalpha()]
    palindromes = set()
    
    for combination in itertools.permutations(english_letters, len(english_letters)):
        current_word = ''.join(combination)
        if current_word == current_word[::-1] and len(current_word) >= 5:
            palindromes.add(current_word)
    
    return palindromes
