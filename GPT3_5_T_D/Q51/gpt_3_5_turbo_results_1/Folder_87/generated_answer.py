
from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter(["".join(sorted(s.lower())) for s in lst if len(s) >= 3 and s.isalpha()])
    pairs = sum(value * (value - 1) // 2 for value in counter.values())
    return pairs <= 392
