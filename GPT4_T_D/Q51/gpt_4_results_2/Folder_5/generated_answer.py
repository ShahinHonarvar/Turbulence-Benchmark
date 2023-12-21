
from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            d[sorted_word].append(word)
    pairs_count = sum(1 for v in d.values() if len(v) > 1)
    return pairs_count <= 4
