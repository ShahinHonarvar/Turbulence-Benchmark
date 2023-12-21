
from collections import Counter

def if_contains_anagrams(lst):
    counts = Counter(tuple(sorted(s.lower())) for s in lst if len(s) >= 3 and s.isalpha())
    return len(counts) <= 257
