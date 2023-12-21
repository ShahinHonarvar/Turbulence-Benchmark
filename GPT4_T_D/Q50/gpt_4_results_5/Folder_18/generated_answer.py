
from collections import Counter

def if_contains_anagrams(lst):
    anagram_pairs = 0
    anagrams = [str(sorted(w.lower())) for w in lst if len(w) >= 3]
    count = list(Counter(anagrams).values())
    for c in count:
        anagram_pairs += c * (c-1) // 2
    if anagram_pairs >= 106:
        return True
    return False
