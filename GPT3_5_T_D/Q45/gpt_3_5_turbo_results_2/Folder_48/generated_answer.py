
import itertools
import re

def palindromes_between_indices(string):
    if len(string) < 9:
        return set()

    letters = re.findall('[A-Za-z]', string[6:9].lower())
    if len(letters) < 4:
        return set()

    all_palindromes = set()

    for i in range(4, len(letters)+1):
        for perm in itertools.permutations(letters, i):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                all_palindromes.add(candidate)

    return all_palindromes
