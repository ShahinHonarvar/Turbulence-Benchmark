
from itertools import permutations

def palindromes_between_indices(string):
    sub_str = string[3:6].lower()
    permutations_list = [''.join(p) for p in permutations(sub_str) if len(p)>=3]
    palindromes = set([i for i in permutations_list if i == i[::-1]])
    return palindromes
