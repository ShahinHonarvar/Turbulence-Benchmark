
from collections import Counter

def if_contains_anagrams(lst):
    sorted_words = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    counts = Counter(sorted_words)
    pairs = sum(1 for count in counts.values() if count > 1)
    return pairs <= 4
