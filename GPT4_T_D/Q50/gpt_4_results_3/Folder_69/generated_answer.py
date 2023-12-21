
from collections import Counter

def if_contains_anagrams(word_list):
    counter = Counter("".join(sorted(word)).lower() for word in word_list if len(word) >= 3)
    pairs = sum(value*(value-1)//2 for value in counter.values())
    return pairs >= 188
