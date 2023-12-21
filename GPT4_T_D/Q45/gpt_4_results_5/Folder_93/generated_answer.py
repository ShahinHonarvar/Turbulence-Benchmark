
from itertools import permutations

def palindromes_between_indices(s):
    letters = s[2:8].lower()
    result = set()
    for i in range(6, len(letters) + 1):
        for perm in permutations(letters, i):
            word = ''.join(perm)
            if word == word[::-1]:
                result.add(word)
    return result
