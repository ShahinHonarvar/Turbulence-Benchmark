
from itertools import permutations

def palindromes_between_indices(s):
    s = s[:5].lower()
    characters = [c for c in s if c.isalpha()]
    palindromes = set()

    for i in range(3, len(characters)+1):
        for perm in permutations(characters, i):
            candidate = "".join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
                
    return palindromes
