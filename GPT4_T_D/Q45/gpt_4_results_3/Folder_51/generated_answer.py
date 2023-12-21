
from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:6].lower()
    possible_palindromes = set()
    for length in range(3, len(s) + 1):
        for permutation in permutations(s, length):
            permutation = "".join(permutation)
            if permutation == permutation[::-1]:
                possible_palindromes.add(permutation)
    return possible_palindromes
