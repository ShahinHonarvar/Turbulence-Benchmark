
from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    words = [''.join(sorted(w.lower())) for w in lst if len(w) >= 3]
    freq_map = Counter(words)
    for k in freq_map:
        count += freq_map[k] * (freq_map[k] - 1) / 2
    if count >= 86:
        return True
    else:
        return False
