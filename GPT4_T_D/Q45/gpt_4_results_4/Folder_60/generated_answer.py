
from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:7].lower()
    palindromes = set()
    for i in range(4, len(s)+1):
        for subset in permutations(s, i):
            subset = ''.join(subset)
            if subset == subset[::-1]:
                palindromes.add(subset)
    return palindromes
