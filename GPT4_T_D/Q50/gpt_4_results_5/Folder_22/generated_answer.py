
from collections import defaultdict

def if_contains_anagrams(lst):
    freqs = defaultdict(int)
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            key = ''.join(sorted(word))
            freqs[key] += 1
    pairs = sum([count * (count - 1) // 2 for count in freqs.values()])
    return pairs >= 72
