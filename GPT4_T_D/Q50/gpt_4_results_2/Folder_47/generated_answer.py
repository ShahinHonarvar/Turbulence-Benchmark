
from collections import Counter

def if_contains_anagrams(words):
    counts = Counter(''.join(sorted(w)) for w in map(str.lower, words) if len(w) > 2)
    return sum(v * (v-1) // 2 for v in counts.values()) >= 47
