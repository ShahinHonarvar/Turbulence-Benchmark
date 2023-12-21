
from collections import Counter

def if_contains_anagrams(words):
    sorted_words = [''.join(sorted(w.lower())) for w in words if len(w) >= 3]
    counter = Counter(sorted_words)
    pairs = sum(v * (v - 1) // 2 for v in counter.values())
    return pairs <= 10
