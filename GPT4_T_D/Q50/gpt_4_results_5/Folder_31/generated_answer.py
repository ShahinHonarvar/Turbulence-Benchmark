
from collections import Counter

def if_contains_anagrams(lst):
    words = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    counts = Counter(words)
    pairs = sum(v*(v-1) // 2 for v in counts.values())
    return pairs >= 68
