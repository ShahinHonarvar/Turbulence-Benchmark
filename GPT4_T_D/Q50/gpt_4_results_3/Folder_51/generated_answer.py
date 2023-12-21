
from collections import Counter

def if_contains_anagrams(str_list):
    str_list = [''.join(sorted(s.lower())) for s in str_list if len(s) >= 3]
    anagram_count = Counter(str_list)
    pairs = 0
    for value in anagram_count.values():
        pairs += (value * (value - 1)) // 2
    return pairs >= 39
