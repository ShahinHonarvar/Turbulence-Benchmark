
from collections import Counter

def if_contains_anagrams(str_list):
    str_list = [''.join(sorted(s.lower())) for s in str_list if len(s) >= 3]
    counts = Counter(str_list)
    pairs = sum([c * (c - 1) / 2 for c in counts.values()])
    return pairs >= 194
