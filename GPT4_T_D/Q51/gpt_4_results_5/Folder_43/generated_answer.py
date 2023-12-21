
from collections import Counter

def if_contains_anagrams(strings):
    freq_counter = Counter(''.join(sorted(s.lower())) for s in strings if len(s) >= 3)
    return sum(v > 1 for v in freq_counter.values()) <= 3
