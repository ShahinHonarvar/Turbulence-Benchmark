
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string if char.isalpha()]
    indexes = range(4)
    palindromes = set()
    
    for length in range(3, len(letters)+1):
        for combination in itertools.combinations(letters, length):
            for permutation in itertools.permutations(combination):
                if permutation == permutation[::-1]:
                    palindromes.add(''.join(permutation))
    
    return palindromes
