
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:9].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()

    for length in range(7, len(letters)+1):
        for perm in permutations(letters, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)

    return palindromes
