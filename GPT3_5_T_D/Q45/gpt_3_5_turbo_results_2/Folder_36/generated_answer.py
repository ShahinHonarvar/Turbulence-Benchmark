
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[5:9] if char.isalpha()]
    palindromes = set()

    for length in range(3, len(letters) + 1):
        for combination in itertools.permutations(letters, length):
            if combination == combination[::-1]:
                palindromes.add(''.join(combination))

    return palindromes
