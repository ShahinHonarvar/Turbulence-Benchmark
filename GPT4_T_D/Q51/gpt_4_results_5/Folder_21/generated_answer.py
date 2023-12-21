
from collections import Counter

def if_contains_anagrams(strings):
    strings = [x.lower() for x in strings if len(x) >= 3]
    counts = Counter(["".join(sorted(s)) for s in strings])
    pairs = sum([v//2 for k, v in counts.items()])
    return pairs <= 26
