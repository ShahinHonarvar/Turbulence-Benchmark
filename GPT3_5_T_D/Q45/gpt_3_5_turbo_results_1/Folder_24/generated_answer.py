
import itertools

def palindromes_between_indices(string):
    string = string.lower()
    letters = [char for char in string[2:10] if char.isalpha()]
    palindromes = set()
    
    for length in range(4, len(letters) + 1):
        for combo in itertools.permutations(letters, length):
            word = ''.join(combo)
            if word == word[::-1]:
                palindromes.add(word)
    
    return palindromes
