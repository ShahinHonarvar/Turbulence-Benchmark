
from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    palindromes = set()
    for l in range(4, len(s)+1):
        for subset in permutations(s, l):
            subset = ''.join(subset)
            if subset == subset[::-1]:
                palindromes.add(subset)
    return palindromes
