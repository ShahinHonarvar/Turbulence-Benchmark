
from collections import defaultdict

def if_contains_anagrams(words):
    d = defaultdict(int)
    for word in words:
        w = ''.join(sorted(word))
        if len(w) >= 3:
            d[w.lower()] += 1
    
    count = sum(v*(v-1)//2 for v in d.values() if v > 1)
    return count <= 64
