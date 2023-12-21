
import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s if c.isalpha()]
    possible_combinations = set(itertools.permutations(letters, 4))
    palindromes = set()
    
    for combination in possible_combinations:
        p = "".join(combination)
        if p == p[::-1]:
            palindromes.add(p)
    
    return palindromes
