
from collections import Counter

def if_contains_anagrams(strings):
    dicts = [str(sorted(s.lower())) for s in strings if len(s) >= 3]
    counter = Counter(dicts)
    pairs = sum(v*(v-1)//2 for v in counter.values()) 
    return pairs >= 86
