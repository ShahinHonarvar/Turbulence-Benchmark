
from collections import defaultdict

def if_contains_anagrams(lst):
    counts = defaultdict(list)
    for word in lst:
        counts["".join(sorted(word.lower()))].append(word)
    pairs = sum((len(words) - 1) * len(words) // 2 for words in counts.values() if len(words) > 1 and len(words[0])>=3)
    return pairs >= 38
