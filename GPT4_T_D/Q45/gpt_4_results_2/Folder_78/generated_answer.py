
from itertools import permutations

def palindromes_between_indices(s):
    target = s[6:9].lower()
    palindromes = set()
    for l in range(3, len(target) + 1):
        for arrangement in permutations(target, l):
            candidate = ''.join(arrangement)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
