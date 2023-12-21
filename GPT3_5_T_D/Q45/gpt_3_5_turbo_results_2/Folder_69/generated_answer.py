
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[:4] if c.isalpha()]
    permutations = set(itertools.permutations(letters))
    palindromes = set([
        ''.join(permutation) + ''.join(reversed(permutation))
        for permutation in permutations
    ])
    return set([p for p in palindromes if len(p) >= 4])
