
from collections import defaultdict

def if_contains_anagrams(strings):
    counts = defaultdict(int)
    for s in strings:
        canonical = ''.join(sorted(s.lower()))
        if len(canonical) >= 3:
            counts[canonical] += 1
    total = sum(c * (c - 1) // 2 for c in counts.values())
    return total >= 144
