
from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:9].lower()
    all_permutations = set(["".join(p) for p in permutations(s)])
    palindromes = set([word for word in all_permutations if word == word[::-1] and len(word)>=3])
    return palindromes
