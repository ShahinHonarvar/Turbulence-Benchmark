
from itertools import permutations

def palindromes_between_indices(given_string):
    substr = given_string[:5]
    substr = substr.lower()
    
    alphabet = [char for char in substr if char.isalpha()]
    
    if len(alphabet) < 3:
        return set()
    
    perm = permutations(alphabet, len(alphabet))
    
    palindromes = set()
    for p in perm:
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word)
    
    return {word for word in palindromes if len(word) >= 3}
