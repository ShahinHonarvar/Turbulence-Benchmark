
from collections import Counter

def if_contains_anagrams(string_list):
    anagrams = Counter(''.join(sorted(s.lower())) for s in string_list if len(s) >= 3)
    pairs = sum(val * (val - 1) // 2 for val in anagrams.values())
    return pairs <= 86
