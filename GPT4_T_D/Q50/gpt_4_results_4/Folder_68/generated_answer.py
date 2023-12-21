
from collections import Counter

def if_contains_anagrams(l):
    cnt = Counter(''.join(sorted(e.lower())) for e in l if len(e) >= 3)
    return sum(v * (v - 1) // 2 for v in cnt.values()) >= 9
