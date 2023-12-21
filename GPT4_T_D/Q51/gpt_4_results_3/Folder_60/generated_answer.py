
from collections import Counter

def if_contains_anagrams(string_list):
    filtered_list = [''.join(sorted(s.lower())) for s in string_list if len(s) >= 3]
    count = Counter(filtered_list)
    anagram_pairs = sum(val * (val - 1) // 2 for val in count.values())
    return anagram_pairs <= 77
