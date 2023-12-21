
import itertools

def palindromes_between_indices(string):
    letters = [letter.lower() for letter in string[3:6] if letter.isalpha()]
    palindromes = []
    
    for perm in itertools.permutations(letters):
        word = ''.join(perm)
        
        if word == word[::-1]:
            palindromes.append(word)
    
    return set(palindromes) if palindromes else set()
