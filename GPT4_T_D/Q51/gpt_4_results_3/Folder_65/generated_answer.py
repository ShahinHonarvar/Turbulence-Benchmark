
from collections import Counter

def if_contains_anagrams(lst):
    word_count = Counter()
    for word in lst:
        sorted_word = "".join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            word_count[sorted_word] += 1
    pair_count = sum((c * (c - 1)) // 2 for c in word_count.values())
    return pair_count <= 72
