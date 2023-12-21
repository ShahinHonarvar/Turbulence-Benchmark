
from collections import Counter

def if_contains_anagrams(str_list):
    sorted_str_list = [''.join(sorted(s.lower())) for s in str_list if len(s) >= 3]
    count = Counter(sorted_str_list)
    anagram_counts = [count for val, count in count.items() if count > 1]
    anagram_pairs = sum([i//2 for i in anagram_counts])
    return anagram_pairs <= 8
