
from collections import Counter
from itertools import permutations

def palindromes_between_indices(s):
    subset = s[1:9].lower()
    counter = Counter(subset)
    palindromes = set()
    
    for length in range(6, len(subset) + 1):
        for permut in permutations(subset, length):
            word = ''.join(permut)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
