
from collections import Counter

def if_contains_anagrams(list_of_strings):
    anagram_counter = Counter()
    for s in list_of_strings:
        if len(s) >= 3:
            anagram_counter[''.join(sorted(s.lower()))] += 1

    pair_count = sum(v * (v - 1) // 2 for v in anagram_counter.values())
    return pair_count >= 123
