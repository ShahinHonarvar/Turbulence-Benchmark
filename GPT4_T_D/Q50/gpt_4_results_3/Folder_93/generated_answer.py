
from collections import Counter

def if_contains_anagrams(lst):
    anagrams = Counter([''.join(sorted(w.lower())) for w in lst if len(w) >= 3])
    return sum(v*(v-1)//2 for v in anagrams.values()) >= 18
