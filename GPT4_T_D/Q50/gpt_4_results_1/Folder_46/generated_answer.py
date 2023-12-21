
from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for s in lst:
        c[''.join(sorted(s.lower()))] += 1
    return sum(val*(val-1) // 2 for val in c.values() if len(list(c.keys())[0]) >= 3) >= 38
