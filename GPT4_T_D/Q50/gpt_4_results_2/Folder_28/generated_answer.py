
from collections import Counter

def if_contains_anagrams(strings):
    counter = Counter()
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            counter[''.join(sorted(s_lower))] += 1
    return sum(v * (v - 1) // 2 for v in counter.values()) >= 81
