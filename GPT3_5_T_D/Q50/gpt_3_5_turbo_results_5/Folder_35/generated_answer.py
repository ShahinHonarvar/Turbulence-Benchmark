
from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter()
    for word in lst:
        counter[str(sorted(word.lower()))] += 1
    count = 0
    for value in counter.values():
        count += value * (value - 1) // 2
    return count >= 153
