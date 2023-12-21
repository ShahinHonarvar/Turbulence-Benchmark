
from itertools import permutations

def palindromes_between_indices(text):
    sub_string = text[5:10].lower()
    palindromes = set()

    for length in range(4, len(sub_string)+1):
        for perm in permutations(sub_string, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)

    return palindromes
