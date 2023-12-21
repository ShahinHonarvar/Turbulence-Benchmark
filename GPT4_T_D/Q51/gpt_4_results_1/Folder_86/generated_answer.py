
from collections import Counter

def if_contains_anagrams(lst):
    sorted_strings = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    counts = Counter(sorted_strings)
    pair_count = sum(val*(val-1)//2 for val in counts.values())
    return pair_count <= 48
