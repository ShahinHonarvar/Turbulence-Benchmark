
from collections import Counter

def if_contains_anagrams(lst):
    counts = Counter()
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            counts[''.join(sorted(word_lower))] += 1
    return sum(v * (v - 1) // 2 for v in counts.values()) >= 36
