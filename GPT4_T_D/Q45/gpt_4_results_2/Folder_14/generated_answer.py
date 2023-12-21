
from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:6].lower()
    found_palindromes = set()

    for i in range(3, len(s) + 1):
        for p in permutations(s, i):
            string_combination = ''.join(p)
            if string_combination == string_combination[::-1]:
                found_palindromes.add(string_combination)

    return found_palindromes
