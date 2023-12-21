
from collections import Counter

def if_contains_anagrams(word_list):
    sorted_words = [''.join(sorted(w.lower())) for w in word_list if len(w) >= 3]
    counts = Counter(sorted_words)
    pairs = sum(val // 2 for val in counts.values())
    return pairs <= 28
