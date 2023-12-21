
from itertools import permutations

def palindromes_between_indices(input_str):
    input_str = input_str[1:7].lower()
    palindromes_set = set()
    for i in range(7, len(input_str) + 1):
        for perm in permutations(input_str, i):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes_set.add(candidate)
    return palindromes_set
