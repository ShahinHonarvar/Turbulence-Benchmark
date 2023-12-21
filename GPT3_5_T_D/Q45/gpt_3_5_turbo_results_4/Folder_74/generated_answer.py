
import itertools

def palindromes_between_indices(s):
    letters = [ch for ch in s[1:7].lower() if ch.isalpha()]
    palindromes = set()
    
    for perm in itertools.permutations(letters, len(letters)):
        word = ''.join(perm)
        if len(word) >= 6 and word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
