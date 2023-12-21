
from itertools import permutations

def palindromes_between_indices(string):
    string = string.lower()[:7]
    palindromes = set()
    
    for r in range(3, len(string) + 1):
        for combo in permutations(string, r):
            combo_string = ''.join(combo)
            if combo_string == combo_string[::-1]:
                palindromes.add(combo_string)
    
    return palindromes
