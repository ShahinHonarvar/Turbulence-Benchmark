
from itertools import permutations

def palindromes_between_indices(s):
    sub_string = s[4:10].lower()
    letters = [char for char in sub_string if char.isalpha()]
    palindromes = set()
    for permutation in permutations(letters):
        joined_permutation = "".join(permutation)
        if joined_permutation == joined_permutation[::-1] and len(joined_permutation) >= 5:
            palindromes.add(joined_permutation)
    
    return palindromes
