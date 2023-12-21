
from itertools import permutations

def palindromes_between_indices(s):
    s = s[7:10].lower()
    s_letters = [char for char in s if char.isalpha()]
    palindromes = set()

    for i in range(4, len(s_letters) + 1):
        for subset in permutations(s_letters, i):
            candidate = ''.join(subset)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)

    return palindromes
