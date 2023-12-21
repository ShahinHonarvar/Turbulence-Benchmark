
import itertools

def palindromes_between_indices(string):
    string = string[:7].lower()
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    
    for length in range(3, len(letters) + 1):
        for combination in itertools.permutations(letters, length):
            if combination == combination[::-1]:
                palindromes.add(''.join(combination).lower())

    return palindromes
