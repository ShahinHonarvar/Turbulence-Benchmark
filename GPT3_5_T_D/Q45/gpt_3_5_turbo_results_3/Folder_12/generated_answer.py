
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string if c.isalpha()]
    letters = letters[3:9] if len(letters) >= 9 else []
    palindromes = set()
    
    for perm in itertools.permutations(letters):
        word = ''.join(perm) + ''.join(reversed(perm))
        if len(word) >= 4 and word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
