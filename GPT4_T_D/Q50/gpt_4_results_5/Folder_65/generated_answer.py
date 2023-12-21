
from collections import Counter

def if_contains_anagrams(words):
    counter = Counter("".join(sorted(word.lower())) for word in words if len(word) >= 3)
    pairs = sum(val*(val-1)//2 for val in counter.values())
    return pairs >= 94
