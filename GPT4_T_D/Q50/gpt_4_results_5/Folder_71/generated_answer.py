
from collections import Counter

def if_contains_anagrams(words):
    counter = Counter([''.join(sorted(s.lower())) for s in words if len(s) >= 3])
    pairs = sum([n*(n-1)//2 for n in counter.values() if n > 1])
    return pairs >= 57
