
import itertools

def palindromes_between_indices(s):
    english_letters = [char for char in s.lower() if char.isalpha()]
    combinations = list(itertools.combinations(english_letters, 3))
    palindromes = set()
    
    for comb in combinations:
        for permutation in itertools.permutations(comb):
            if permutation == permutation[::-1]:
                palindromes.add(''.join(permutation))
    
    return palindromes
