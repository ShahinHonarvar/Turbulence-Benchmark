
from collections import Counter
from itertools import combinations

def if_contains_anagrams(lst):
    words = ["".join(sorted(word.lower())) for word in lst if len(word) >= 3]
    counter = Counter(words)
    pairs = [comb for word, count in counter.items() for comb in combinations([word]*count, 2)]
    return len(pairs) >= 7
