
import itertools

def palindromes_between_indices(string):
    letters = [ch.lower() for ch in string[:6] if ch.isalpha()]
    palindromes = set()
    
    for length in range(4, len(letters) + 1):
        for combination in itertools.permutations(letters, length):
            if combination == combination[::-1]:
                palindromes.add(''.join(combination))
    
    return palindromes
