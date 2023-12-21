
from collections import Counter

def if_contains_anagrams(lst):
    count = Counter("".join(sorted(word.lower())) for word in lst if len(word) >= 3)
    return sum(value * (value-1) // 2 for value in count.values()) >= 276
