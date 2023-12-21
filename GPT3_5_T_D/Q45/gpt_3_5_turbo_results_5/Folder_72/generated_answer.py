
import itertools

def palindromes_between_indices(string):
    letters = [ch.lower() for ch in string[1:8] if ch.isalpha()]
    count = len(letters)
    
    if count < 6:
        return set()
    
    palindromes = []
    
    for perm in itertools.permutations(letters, count):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.append(word)
            
    return set(palindromes)
