
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string if c.isalpha()]
    letters_range = letters[4:10]
    perms = set(itertools.permutations(letters_range))
    palindromes = set()
    for perm in perms:
        if perm == perm[::-1]:
            palindromes.add(''.join(perm))
    return palindromes
