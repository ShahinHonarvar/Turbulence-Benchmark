
import itertools

def palindromes_between_indices(string):
    english_letters = [c for c in string.lower() if c.isalpha()]
    valid_letters = set(english_letters[:7])
    
    palindromes = set()
    for perm in itertools.permutations(valid_letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    
    return palindromes
