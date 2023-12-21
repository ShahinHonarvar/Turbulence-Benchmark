
from itertools import permutations

def palindromes_between_indices(string):
    string = string[4:9].lower()
    palindromes = set()
    for permutation in permutations(string):
        combined = ''.join(permutation)
        if len(combined) >= 6 and combined == combined[::-1]:
            palindromes.add(combined)
    return palindromes
