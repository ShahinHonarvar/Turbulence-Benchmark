
from collections import Counter

def if_contains_anagrams(lst):
    anagram_counter = Counter()
    for word in lst:
        if len(word) >= 3:
            anagram_counter[''.join(sorted(word.lower()))] += 1
    return sum(v * (v - 1) // 2 for v in anagram_counter.values()) >= 68
