
from itertools import permutations

def palindromes_between_indices(string):
    string = string.lower()
    sub_string = string[0:5]
    perm = [''.join(p) for p in permutations(sub_string)]
    palindromes = set()
    for word in perm:
        if len(word) >= 4 and word == word[::-1]:
            palindromes.add(word)
    return palindromes
