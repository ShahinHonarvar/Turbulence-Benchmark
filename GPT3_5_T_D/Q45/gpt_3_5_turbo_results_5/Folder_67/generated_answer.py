
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[2:7] if c.isalpha()]
    permutations = list(set(''.join(p) for p in itertools.permutations(letters, len(letters))) if len(letters) >= 5 else [])
    palindromes = set(p for p in permutations if p.lower() == p[::-1].lower() and len(p) >= 5)
    return palindromes
