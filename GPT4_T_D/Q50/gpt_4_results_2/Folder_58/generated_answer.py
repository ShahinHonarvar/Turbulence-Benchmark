
from collections import Counter

def if_contains_anagrams(lst):
    if len(lst) < 2:
        return False
    ctr = Counter([''.join(sorted(s.lower())) for s in lst if len(s) >= 3])
    return sum(v * (v-1) // 2 for v in ctr.values()) >= 411
