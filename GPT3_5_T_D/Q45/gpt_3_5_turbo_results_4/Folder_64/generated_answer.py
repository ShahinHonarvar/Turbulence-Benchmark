
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[4:10] if c.isalpha()]
    unique_letters = list(set(letters))
    palindromes = set()
    
    for combination in itertools.combinations_with_replacement(unique_letters, 6):
        perms = [''.join(p) for p in itertools.permutations(combination, 6)]
        for perm in perms:
            if perm == perm[::-1]:
                palindromes.add(perm)
    
    return palindromes
