
from collections import Counter

def if_contains_anagrams(lst):
    sorted_words = [''.join(sorted(w.lower())) for w in lst if len(w) >= 3]
    counter = Counter(sorted_words)
    pair_count = 0
    for k, v in counter.items():
        pair_count += v * (v - 1) // 2
    return pair_count <= 392
