
from collections import Counter

def if_contains_anagrams(lst):
    words_counter = {}
    for string in lst:
        str_lower = string.lower()
        if len(str_lower) < 3:
            continue
        sorted_str = ''.join(sorted(str_lower))
        if sorted_str not in words_counter:
            words_counter[sorted_str] = 0
        words_counter[sorted_str] += 1
    anagram_pairs = sum(val*(val-1)//2 for val in words_counter.values() if val > 1)
    return anagram_pairs >= 94
