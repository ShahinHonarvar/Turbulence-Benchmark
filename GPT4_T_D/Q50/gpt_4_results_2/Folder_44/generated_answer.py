
from collections import Counter

def if_contains_anagrams(lst):
    freq_map = Counter([''.join(sorted(s.lower())) for s in lst if len(s) >= 3])
    pairs = sum([v * (v-1) // 2 for v in freq_map.values()])
    return pairs >= 44
