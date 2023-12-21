
import itertools

def palindromes_between_indices(string):
    letters = [ch for ch in string.lower() if ch.isalpha()]
    palindromes = set()
    
    for length in range(7, 9):
        for combination in itertools.combinations(letters, length):
            if combination == combination[::-1]:
                palindromes.add(''.join(combination))
    
    return palindromes
