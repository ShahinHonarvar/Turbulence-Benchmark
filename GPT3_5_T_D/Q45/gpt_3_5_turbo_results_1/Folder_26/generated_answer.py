
import itertools

def palindromes_between_indices(string):
    english_letters = [c for c in string if c.isalpha()]
    english_letters = [c.lower() for c in english_letters]
    english_letters = english_letters[3:7]
    
    palindromes = set()
    for r in range(3, len(english_letters) + 1):
        perm = itertools.permutations(english_letters, r)
        for p in perm:
            if p == p[::-1]:
                palindromes.add(''.join(p))

    return palindromes
