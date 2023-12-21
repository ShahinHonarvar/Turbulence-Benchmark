
from collections import defaultdict

def if_contains_anagrams(words):
    d = defaultdict(list)
    for word in words:
        d[''.join(sorted(word.lower()))].append(word)
    pairs = 0
    for v in d.values():
        if len(v) > 1 and len(v[0]) >= 3:
            pairs += len(v) * (len(v) - 1) // 2
    return pairs <= 113
