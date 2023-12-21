
from collections import Counter

def count_anagrams(lst):
    cnt = Counter()
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            cnt[tuple(sorted(word))] += 1

    return sum(value * (value - 1) // 2 for value in cnt.values())

def if_contains_anagrams(lst):
    return count_anagrams(lst) >= 155
