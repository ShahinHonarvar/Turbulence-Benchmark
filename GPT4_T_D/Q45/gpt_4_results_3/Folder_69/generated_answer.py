
from itertools import permutations

def palindromes_between_indices(str):
    substring = str[0:4].lower()
    palindromes = set()
    for l in range(4, len(substring) + 1):
        for permutation in permutations(substring, l):
            permutation = ''.join(permutation)
            if permutation == permutation[::-1]:
                palindromes.add(permutation)
          
    return palindromes
