
from collections import Counter

def if_contains_anagrams(lst):
    word_counts = Counter(word.lower() for word in lst if len(word) >= 3)
    anagram_counts = sum(val * (val-1) // 2 for val in word_counts.values())
    return anagram_counts >= 10
