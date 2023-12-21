
from collections import Counter

def if_contains_anagrams(string_list):
    sorted_strings = [''.join(sorted(s.lower())) for s in string_list if len(s) >= 3]
    counter = Counter(sorted_strings)
    anagram_pairs = sum(v * (v-1) // 2 for v in counter.values())
    return anagram_pairs <= 279
