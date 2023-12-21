
import itertools

def palindromes_between_indices(string):
    letters = [ch for ch in string[:3].lower() if ch.isalpha()]
    perms = set(''.join(perm) for perm in itertools.permutations(letters))
    palindromes = set(word.lower() for word in perms if len(word) >= 3 and word == word[::-1])
    
    return palindromes
