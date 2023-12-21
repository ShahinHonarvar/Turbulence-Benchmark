
from collections import Counter

def if_contains_anagrams(lst):
    sorted_words = [''.join(sorted(w.lower())) for w in lst if len(w) >= 3]
    counts = Counter(sorted_words)
    pairs = sum(v*(v-1)//2 for v in counts.values())
    return pairs <= 21
