
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:9]
    res = set()
    for length in range(4, len(s)+1):
        for p in permutations(s, length):
            word = ''.join(p)
            if word.lower() == word[::-1].lower():
                res.add(word.lower())
    return res
