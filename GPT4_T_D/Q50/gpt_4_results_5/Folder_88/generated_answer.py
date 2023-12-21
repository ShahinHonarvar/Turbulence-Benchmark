
from collections import Counter

def if_contains_anagrams(lst):
    normalized_words = [''.join(sorted(w.lower())) for w in lst if len(w) >= 3]
    counts = Counter(normalized_words)
    pairs = sum([c // 2 for c in counts.values()])
    return pairs >= 34
