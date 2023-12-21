
from collections import Counter

def if_contains_anagrams(lst):
    str_counts = Counter("".join(sorted(s.lower())) for s in lst if len(s) >= 3)
    pair_counts = sum(v * (v - 1) // 2 for v in str_counts.values())
    return pair_counts >= 65
