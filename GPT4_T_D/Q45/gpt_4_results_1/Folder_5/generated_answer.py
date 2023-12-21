
from itertools import permutations

def palindromes_between_indices(string):
    letters = string[4:9]
    result = set()
    for length in range(4, len(letters) + 1):
        for word in permutations(letters, length):
            word = ''.join(word).lower()
            if word == word[::-1]:
                result.add(word)
    return result
