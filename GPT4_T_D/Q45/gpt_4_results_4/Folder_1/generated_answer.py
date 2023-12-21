
from itertools import permutations

def palindromes_between_indices(s):
    sub_string = s[4:8].lower()
    perms = [''.join(p) for p in permutations(sub_string)]
    palindromes = set()
    for word in perms:
        if len(word) >= 5 and word == word[::-1]:
            palindromes.add(word)
    return palindromes
