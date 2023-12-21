
from collections import Counter

def if_contains_anagrams(lst):
    freq = Counter(tuple(sorted(set(word.lower()))) for word in lst if len(word) >= 3)
    pair_count = sum(val*(val-1)//2 for val in freq.values())
    return pair_count >= 73
