
import itertools

def palindromes_between_indices(string):
    letters = [char for char in string[2:7] if char.isalpha()]
    permutations = [''.join(p) for p in itertools.permutations(letters)]
    palindromes = {p for p in permutations if p.lower() == p.lower()[::-1] and len(p) >= 5}
    return palindromes
