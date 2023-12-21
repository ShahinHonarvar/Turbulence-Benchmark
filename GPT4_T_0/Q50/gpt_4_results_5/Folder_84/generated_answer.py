
from collections import Counter

def if_contains_anagrams(lst):
    anagram_counter = Counter()
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_counter[sorted_word] += 1
    pairs = sum(count * (count - 1) // 2 for count in anagram_counter.values())
    return pairs >= 108
