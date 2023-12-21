
from itertools import permutations

def palindromes_between_indices(in_string):
    val_string = in_string[1:5].lower()
    candidates = {''.join(p) for p in permutations(val_string) if len(p) >= 4}
    return {p for p in candidates if p == p[::-1]}
