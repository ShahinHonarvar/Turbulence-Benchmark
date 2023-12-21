
import itertools

def palindromes_between_indices(string):
    english_letters = [c.lower() for c in string if c.isalpha()]
    palindromes = set()
    for length in range(3, len(english_letters)+1):
        for combination in itertools.combinations(english_letters, length):
            if combination == combination[::-1]:
                palindromes.add(''.join(combination))
    return palindromes
