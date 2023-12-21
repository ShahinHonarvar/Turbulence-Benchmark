
import itertools

def palindromes_between_indices(string):
    letters = ''.join(filter(str.isalpha, string[4:6])).lower()
    palindromes = set()
    
    for length in range(3, len(letters) + 1):
        for combination in itertools.permutations(letters, length):
            word = ''.join(combination)
            if word.lower() == word.lower()[::-1]:
                palindromes.add(word)
    
    return palindromes
