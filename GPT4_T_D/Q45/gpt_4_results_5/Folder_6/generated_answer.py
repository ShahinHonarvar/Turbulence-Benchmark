
from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:8]
    letters = set(s.lower())
    palindromes = set()

    for letter in letters:
        for length in range(4, 9):
            for perm in permutations(s, length):
                candidate = ''.join(perm)
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes
