
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:9].lower()
    palindromes = set()
    for length in range(6, len(s)+1):
        for subset in permutations(s, length):
            subset = ''.join(subset)
            if subset == subset[::-1]:
                palindromes.add(subset)
    return palindromes
