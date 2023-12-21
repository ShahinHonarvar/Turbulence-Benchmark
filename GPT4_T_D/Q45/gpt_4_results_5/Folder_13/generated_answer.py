
from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:10].lower()
    letters = [c for c in s if c.isalpha()]
    res = set()
    for i in range(5, len(letters)+1):
        for perm in permutations(letters, i):
            word = ''.join(perm)
            if word == word[::-1]:
                res.add(word)
    return res
