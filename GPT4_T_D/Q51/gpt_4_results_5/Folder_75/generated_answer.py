
from collections import Counter

def if_contains_anagrams(lst):
    counts = Counter()
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            counts[''.join(sorted(word))] += 1
    pair_count = sum([count * (count - 1) // 2 for count in counts.values()])
    return pair_count <= 55
