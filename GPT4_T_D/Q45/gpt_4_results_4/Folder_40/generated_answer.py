
from itertools import permutations

def palindromes_between_indices(string):
    substr = string[4:10].lower()

    letters = set(substr)
    palindromes = set()
    for let in letters:
        for perm in permutations(substr):
            candidate = "".join(perm)
            if len(candidate) < 7:
                continue
            if candidate == candidate[::-1]:
                palindromes.add(candidate)

    return palindromes
