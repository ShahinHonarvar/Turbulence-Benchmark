
from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter()
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            counter[''.join(sorted(word))] += 1

    return sum(v // 2 for v in counter.values()) >= 7
