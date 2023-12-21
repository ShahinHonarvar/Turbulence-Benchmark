
import itertools

def palindromes_between_indices(string):
    letters = [l.lower() for l in string if l.isalpha()]
    palindromes = set()
    
    for combination in itertools.permutations(letters[:7], 7):
        word = ''.join(combination)
        if word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
