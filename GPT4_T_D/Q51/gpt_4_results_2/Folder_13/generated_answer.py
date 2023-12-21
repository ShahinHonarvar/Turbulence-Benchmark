
from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        sorted_word = "".join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams[sorted_word].append(word)
    pair_count = 0
    for pair in anagrams.values():
        pair_count += len(pair) // 2
    return pair_count <= 54
