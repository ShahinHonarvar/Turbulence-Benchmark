
import itertools

def palindromes_between_indices(string):
    result = set()
    characters = [c.lower() for c in string[:6] if c.isalpha()]
    permutations = set(itertools.permutations(characters))
    
    for p in permutations:
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 3:
            result.add(word)
    
    return result
