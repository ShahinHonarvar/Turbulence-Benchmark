
import itertools

def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    combinations = itertools.combinations(letters, 5)
    palindromes = set()
    
    for combo in combinations:
        permuts = itertools.permutations(combo)
        for permut in permuts:
            word = ''.join(permut).lower()
            if word == word[::-1]:
                palindromes.add(word)
    
    return palindromes
