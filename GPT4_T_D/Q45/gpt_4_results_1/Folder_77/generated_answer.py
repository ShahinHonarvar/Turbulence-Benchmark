
from itertools import permutations

def palindromes_between_indices(s):
    unique_letters = set(s[4:7])
    all_possible = [''.join(p).lower() for p in permutations(''.join(unique_letters))]

    return set(x for x in all_possible if len(x) >= 4 and x == x[::-1])
