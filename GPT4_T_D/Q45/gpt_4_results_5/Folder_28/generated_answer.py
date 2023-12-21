
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:6].lower()
    palindromes = set()
    for length in range(4, len(s) + 1):
        for combination in permutations(s, length):
            phrase = ''.join(combination)
            if phrase == phrase[::-1]:
                palindromes.add(phrase)
    return palindromes
