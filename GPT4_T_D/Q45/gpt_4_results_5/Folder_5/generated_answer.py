
from itertools import permutations

def palindromes_between_indices(s):
    sub_string = s[4:9].lower()
    sets = set()
    for length in range(4, len(sub_string) + 1):
        for p in permutations(sub_string, length):
            if ''.join(p) == ''.join(reversed(p)):
                sets.add(''.join(p))
    return sets
