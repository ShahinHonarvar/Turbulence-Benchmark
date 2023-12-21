
from collections import Counter
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:8].lower()
    letters = Counter(s)
    palindromes = set()
    
    for i in range(7, len(s) + 1):
        for combination in permutations(s, i):
            word = ''.join(combination)
            if word == word[::-1]:
                palindromes.add(word)

    return palindromes
