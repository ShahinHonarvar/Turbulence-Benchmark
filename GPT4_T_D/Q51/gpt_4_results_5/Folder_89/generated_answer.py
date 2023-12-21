
from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            anagrams[sorted_s].append(s)
    
    pairs_count = sum(len(v) * (len(v) - 1) // 2 for v in anagrams.values())
    return pairs_count <= 73
