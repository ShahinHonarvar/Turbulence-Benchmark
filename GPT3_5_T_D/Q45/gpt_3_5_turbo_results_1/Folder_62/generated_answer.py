
import itertools
import string

def palindromes_between_indices(string):
    letters = [c.lower() for c in string if c.lower() in string.ascii_letters]
    combinations = set(''.join(comb) for comb in itertools.permutations(letters, len(letters)) if len(comb) >= 7)
    palindromes = set()
    for comb in combinations:
        if comb == comb[::-1]:
            palindromes.add(comb)
    
    return palindromes
