
from collections import Counter

def if_contains_anagrams(str_list):
    anagram_counter = Counter(["".join(sorted(x.lower())) for x in str_list if len(x) >= 3])
    anagram_pairs = sum([val * (val - 1) // 2 for val in anagram_counter.values()])
    return anagram_pairs >= 42
