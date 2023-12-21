
from itertools import permutations

def palindromes_between_indices(string):
    substr = string[1:9]
    letters = [letter.lower() for letter in substr if letter.isalpha()]
    palindromes = set()
    for i in range(6, len(letters) + 1):
        for perm in permutations(letters, i):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
