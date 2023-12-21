
from itertools import permutations

def palindromes_between_indices(string):
    lower_string = string.lower()
    letters = [char for char in lower_string[:6] if char.isalpha()]
    palindromes = {"".join(p) for p in permutations(letters) if len(p) >= 5 and "".join(p) == "".join(reversed(p))}
    return palindromes
