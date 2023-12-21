
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[1:8] if c.isalpha()]
    perms = set(itertools.permutations(letters))
    palindromes = {"".join(p) for p in perms if "".join(p).lower() == "".join(p[::-1]).lower()}
    return {p for p in palindromes if len(p) >= 6}
