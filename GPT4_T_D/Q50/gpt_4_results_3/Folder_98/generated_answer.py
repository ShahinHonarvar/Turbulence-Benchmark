
from collections import Counter

def if_contains_anagrams(lst):
    dict_count = Counter("".join(sorted(word.lower())) for word in lst if len(word) >= 3)
    anagram_pairs = sum(val * (val - 1) // 2 for val in dict_count.values())
    return anagram_pairs >= 7
