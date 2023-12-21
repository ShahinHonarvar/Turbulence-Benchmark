
from collections import Counter

def if_contains_anagrams(lst):
    anagrams = Counter()
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            anagrams[tuple(sorted(s))] += 1
    return sum(value // 2 for value in anagrams.values()) >= 7
