
from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter()
    for word in lst:
        if len(word) >= 3:
            counter[''.join(sorted(word.lower()))] += 1
    return sum(v * (v - 1) // 2 for v in counter.values()) >= 89
