
from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            anagrams[sorted_word].append(word)

    pairs_count = sum(len(v) * (len(v) - 1) // 2 for v in anagrams.values())

    return pairs_count <= 50
