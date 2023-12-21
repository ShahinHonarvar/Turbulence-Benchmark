
from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter(''.join(sorted(s.lower())) for s in lst if len(s) >= 3)
    pairs = sum(v * (v - 1) // 2 for v in counter.values())
    return pairs >= 35
