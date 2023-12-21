
from collections import Counter

def if_contains_anagrams(strs):
    strs = ["".join(sorted(s.lower())) for s in strs if len(s) >= 3]
    freq = Counter(strs)
    pairs = sum([v*(v-1)//2 for v in freq.values()])
    return pairs >= 79
