
import itertools

def palindromes_between_indices(string):
    english_letters = [char.lower() for char in string if char.isalpha()]
    palindromes = set()

    for length in range(4, len(english_letters) + 1):
        for combination in itertools.combinations(english_letters, length):
            if combination == combination[::-1]:
                palindromes.add(''.join(combination))
    
    return palindromes
