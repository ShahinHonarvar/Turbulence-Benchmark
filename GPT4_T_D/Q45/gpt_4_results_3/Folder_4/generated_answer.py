
from itertools import permutations

def palindromes_between_indices(input_str):
    substring = input_str[3:10].lower()
    result = set()
    for perm in permutations(substring):
        candidate = ''.join(perm)
        if len(candidate) < 7:
            continue
        if candidate == candidate[::-1]:
            result.add(candidate)
    return result
