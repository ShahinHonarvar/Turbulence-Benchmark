
from collections import Counter

def if_contains_anagrams(words):
    words = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    counts = Counter(words)
    pairs = 0
    for word in counts:
        pairs += counts[word] * (counts[word] - 1) // 2
    return pairs <= 96
