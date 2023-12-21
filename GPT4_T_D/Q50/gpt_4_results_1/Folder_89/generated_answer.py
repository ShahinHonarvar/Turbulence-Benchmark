
from itertools import combinations
from collections import defaultdict

def if_contains_anagrams(words):
    freqs = defaultdict(list)
    for word in words:
        key = "".join(sorted(word.lower()))
        if len(key) >= 3:
            freqs[key].append(word)

    pairs = 0
    for same, group in freqs.items():
        for combo in combinations(group, 2):
            pairs += 1
            if pairs >= 36:
                return True
    return False
