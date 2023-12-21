
from collections import Counter

def if_contains_anagrams(word_list):
    word_counter = Counter()
    for word in word_list:
        word = word.lower()
        if len(word) >= 3:
            word_counter[tuple(sorted(word))] += 1
    pairs = sum(x * (x - 1) // 2 for x in word_counter.values())
    return pairs >= 143
