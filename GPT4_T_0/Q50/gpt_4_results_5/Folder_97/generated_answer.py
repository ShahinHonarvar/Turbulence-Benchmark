
from collections import Counter

def if_contains_anagrams(lst):
    anagram_counter = Counter()
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_counter[sorted_word] += 1
    pairs = sum(val // 2 for val in anagram_counter.values())
    return pairs >= 123
