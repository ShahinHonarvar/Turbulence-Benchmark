
from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter([''.join(sorted(w.lower())) for w in lst if len(w) >= 3])
    anagram_pairs = sum([v * (v - 1) // 2 for v in counter.values() if v > 1])
    return anagram_pairs >= 15
