
from collections import Counter

def if_contains_anagrams(lst):
    lst = [''.join(sorted(w)) for w in lst if len(w) >= 3]
    cnt = Counter(lst)
    pairs = sum(v*(v-1)//2 for v in cnt.values())
    return pairs >= 97
