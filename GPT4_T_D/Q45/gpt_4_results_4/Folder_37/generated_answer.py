
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:5].lower()
    permutations_list = ["".join(i) for i in permutations(s)]
    palindromes = set()
    for i in permutations_list:
        if i == i[::-1] and len(i) >= 5:
            palindromes.add(i)
    return palindromes
