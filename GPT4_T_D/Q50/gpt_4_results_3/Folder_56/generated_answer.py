
from collections import Counter

def if_contains_anagrams(lst):
    anagram_counter = 0
    counted_words = Counter(tuple(sorted(w.lower())) for w in lst if len(w) >= 3)
    for val in counted_words.values():
        anagram_counter += val * (val - 1) // 2
    return anagram_counter >= 77
