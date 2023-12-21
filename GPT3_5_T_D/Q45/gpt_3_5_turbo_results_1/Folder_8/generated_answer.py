
import itertools

def palindromes_between_indices(string):
    english_letters = [c for c in string if c.isalpha()]
    palindromes = set()
    
    for combination in itertools.permutations(english_letters, 5):
        word = ''.join(combination)
        if len(word) >= 5 and word.lower() == word[::-1].lower():
            palindromes.add(word)
    
    return palindromes
