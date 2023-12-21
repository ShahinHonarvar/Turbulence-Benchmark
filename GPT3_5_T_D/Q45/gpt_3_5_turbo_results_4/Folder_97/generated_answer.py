
import itertools

def palindromes_between_indices(string):
    english_letters = [char.lower() for char in string if char.isalpha()]
    palindromes = set()
    
    for perm in itertools.permutations(english_letters, len(english_letters)):
        substring = ''.join(perm)[:5]
        if substring == substring[::-1] and len(substring) >= 3:
            palindromes.add(substring)
    
    return palindromes
