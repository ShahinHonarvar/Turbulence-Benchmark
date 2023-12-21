
from collections import Counter
import itertools

def if_contains_anagrams(lst):
    c = Counter(''.join(sorted(s.lower())) for s in lst if len(s)>2)
    pairs = sum(v*(v-1)//2 for v in c.values())
    return pairs >= 314
