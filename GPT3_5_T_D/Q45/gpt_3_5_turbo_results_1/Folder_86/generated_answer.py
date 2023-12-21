
import itertools

def palindromes_between_indices(string):
    english_letters = [char.lower() for char in string if char.isalpha()]
    english_letters.sort() 
    english_letters = "".join(english_letters)
    palindromes = set()
    
    for length in range(4, len(english_letters) + 1):
        for permutation in itertools.permutations(english_letters, length):
            word = "".join(permutation)
            if word == word[::-1]:
                palindromes.add(word.lower())
    
    return palindromes
