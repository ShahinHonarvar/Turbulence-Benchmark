
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[5:10] if c.isalpha()]
    palindromes = {"".join(p) for p in itertools.permutations(letters, len(letters))}
    return {p for p in palindromes if p.lower() == p.lower()[::-1] and len(p) >= 6}
