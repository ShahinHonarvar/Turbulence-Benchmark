
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string if char.isalpha()]
    combinations = set([''.join(combo).lower() for combo in itertools.permutations(letters, 5)])
    palindromes = set()
    
    for combo in combinations:
        if combo == combo[::-1]:
            palindromes.add(combo)
    
    return palindromes
