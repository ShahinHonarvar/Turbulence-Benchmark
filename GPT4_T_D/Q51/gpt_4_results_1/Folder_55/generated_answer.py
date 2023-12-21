
from collections import defaultdict

def if_contains_anagrams(lst):
    counter = defaultdict(int)
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            counter["".join(sorted(word))] += 1
    pairs = sum(value // 2 for value in counter.values())
    return pairs <= 44
