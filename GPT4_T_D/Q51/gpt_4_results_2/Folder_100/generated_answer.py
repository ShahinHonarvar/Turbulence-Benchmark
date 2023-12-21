
from collections import Counter

def if_contains_anagrams(lst):
    freq = Counter(''.join(sorted(s.lower())) for s in lst if len(s) >= 3)
    return sum(n * (n - 1) // 2 for n in freq.values()) <= 98
