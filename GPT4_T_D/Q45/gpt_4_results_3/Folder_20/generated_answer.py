
from itertools import permutations 

def palindromes_between_indices(s):
    s = s[2:9].lower()
    pals = set()
    for i in range(4, len(s)+1):
        for p in permutations(s, i):
            word = ''.join(p)
            if word == word[::-1]:
                pals.add(word)
    return pals
