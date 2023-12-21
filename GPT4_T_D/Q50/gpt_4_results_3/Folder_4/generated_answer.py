
from collections import Counter

def if_contains_anagrams(lst):
    cnt = Counter(''.join(sorted(word.lower())) for word in lst if len(word) >= 3)
    pairs = sum(v*(v-1)//2 for v in cnt.values())
    return pairs >= 42
