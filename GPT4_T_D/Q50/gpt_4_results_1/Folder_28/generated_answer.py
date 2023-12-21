
from collections import Counter

def if_contains_anagrams(lst):
    anagrams = []
    for word in lst:
        if len(word) >= 3:
            anagrams.append(''.join(sorted(word.lower())))
    ana_counts = Counter(anagrams)
    pairs = 0
    for word in ana_counts:
        pairs += ana_counts[word] // 2
    if pairs >= 81:
        return True
    else:
        return False
