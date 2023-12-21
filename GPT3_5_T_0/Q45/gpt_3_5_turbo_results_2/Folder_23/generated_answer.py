
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string if c.isalpha()]
    letters = letters[:7]
    palindromes = set()
    
    for length in range(4, len(letters) + 1):
        for combination in itertools.permutations(letters, length):
            word = ''.join(combination)
            if word == word[::-1]:
                palindromes.add(word)
    
    return palindromes
