
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[1:4] if c.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()
    for perm in itertools.permutations(letters, 4):
        if ''.join(perm).lower() == ''.join(perm[::-1]).lower():
            palindromes.add(''.join(perm))
    return palindromes
