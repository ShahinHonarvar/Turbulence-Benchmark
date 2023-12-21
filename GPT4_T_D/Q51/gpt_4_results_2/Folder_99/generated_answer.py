
from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    lst = [''.join(sorted(w.lower())) for w in lst if len(w) >= 3]
    counter = dict(Counter(lst))
    for v in counter.values():
        if v > 1:
            count += v * (v - 1) // 2
    return count <= 93
