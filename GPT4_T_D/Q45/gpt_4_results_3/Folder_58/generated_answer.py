
from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    palindromes = set()
    for length in range(6, len(s)+1):
        for perm in permutations(s,length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
