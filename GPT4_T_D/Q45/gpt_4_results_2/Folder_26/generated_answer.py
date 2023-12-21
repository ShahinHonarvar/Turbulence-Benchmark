
import itertools

def palindromes_between_indices(input_string):
    input_string = input_string[4:7].lower()
    permutations = set(map(''.join, itertools.permutations(input_string)))
    return {p for p in permutations if len(p) >= 3 and p == p[::-1]}
