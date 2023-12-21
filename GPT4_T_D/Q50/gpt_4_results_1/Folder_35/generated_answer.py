
from collections import Counter

def if_contains_anagrams(lst):
    counts = Counter()
    for word in lst:
        if len(word) >= 3:
            counts[str(sorted(word.lower()))] += 1
    total_pairs = sum(v * (v - 1) // 2 for v in counts.values())
    return total_pairs >= 153
