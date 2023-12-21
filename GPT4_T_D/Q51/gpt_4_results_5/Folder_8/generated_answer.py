
from collections import Counter

def if_contains_anagrams(lst):
    str_dict = {}
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            key = tuple(sorted(Counter(s_lower).items()))
            str_dict[key] = str_dict.get(key, 0) + 1
    pairs = sum(val*(val-1)//2 for val in str_dict.values())
    return pairs <= 68
