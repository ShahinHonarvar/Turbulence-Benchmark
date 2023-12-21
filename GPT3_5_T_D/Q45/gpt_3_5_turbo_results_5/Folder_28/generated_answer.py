
import itertools

def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha()]
    palindromes = set()
    
    for length in range(4, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            if combination == combination[::-1]:
                palindromes.add(''.join(combination))
    
    return palindromes
