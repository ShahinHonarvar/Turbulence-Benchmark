
from collections import defaultdict

def if_contains_anagrams(word_list):
    anagrams = defaultdict(set)
    for word in word_list:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            anagrams[''.join(sorted(word_lower))].add(word_lower)
    anagram_pairs = sum(1 for v in anagrams.values() if len(v) > 1)
    return anagram_pairs >= 26
