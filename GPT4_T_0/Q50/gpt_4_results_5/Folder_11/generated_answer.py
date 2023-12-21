
from collections import Counter

def if_contains_anagrams(lst):
    anagram_counter = Counter()
    for word in lst:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            anagram_counter[sorted_word] += 1
    return sum(value >= 2 for value in anagram_counter.values()) >= 28
