
from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            c[tuple(sorted(word))] += 1

    pairs = sum(i*(i-1)//2 for i in c.values())
    return pairs >= 143
