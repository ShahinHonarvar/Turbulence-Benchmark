
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    sub_string = s[2:5]
    permutations_set = set([''.join(permutation) for permutation in permutations(sub_string) if len(permutation) >= 3])
    palindromes_set = set([s for s in permutations_set if s == s[::-1]])
    return palindromes_set
