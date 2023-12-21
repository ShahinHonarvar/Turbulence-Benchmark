
import itertools

def palindromes_between_indices(string):
    letters = ''.join(filter(str.isalpha, string[2:6].lower()))
    palindromes = set()
    
    for comb in itertools.permutations(letters, len(letters)):
        word = ''.join(comb)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    
    return palindromes
