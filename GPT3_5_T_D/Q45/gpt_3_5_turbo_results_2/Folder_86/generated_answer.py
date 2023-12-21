
import itertools

def palindromes_between_indices(string):
    english_letters = [c for c in string if c.isalpha()]
    sub_string = ''.join(english_letters[6:10])
    permutations = set(itertools.permutations(sub_string.upper()))
    
    palindromes = set()
    for perm in permutations:
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    
    return palindromes
