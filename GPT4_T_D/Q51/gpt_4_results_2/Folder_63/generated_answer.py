
from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        word_lower = word.lower()
        sorted_word = ''.join(sorted(word_lower))
        if len(word_lower) >= 3:
            anagrams[sorted_word].append(word_lower)

    anagram_count = sum(len(list(combinations(val, 2))) for val in anagrams.values())
    return anagram_count <= 423
