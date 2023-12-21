
import itertools

def palindromes_between_indices(string):
    letters = [c for c in string[2:8] if c.isalpha()]
    perms = set(itertools.permutations(letters, len(letters)))
    palindromes = {"".join(p).lower() for p in perms if "".join(p).lower() == "".join(p).lower()[::-1] and len(p) >= 6}
    return palindromes
