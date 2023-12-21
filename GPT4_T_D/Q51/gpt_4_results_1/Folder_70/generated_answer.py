
from collections import Counter


def if_contains_anagrams(lst):
    anagrams = []
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            word = ''.join(sorted(word))
            anagrams.append(word)
    counter = Counter(anagrams)
    pairs = 0
    for k, v in counter.items():
        pairs += v * (v-1) // 2
    return pairs <= 97
