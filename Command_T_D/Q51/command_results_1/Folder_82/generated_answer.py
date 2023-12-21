import collections
import re
def if_contains_anagrams(words):
    anagrams = collections.defaultdict(set)
    for word in words:
        if len(word) < 3:
            continue
        for match in ANAGRAM_REGEX.finditer(word):
            anagrams[match.group()].add(word)
    return len(anagrams) <= 40
