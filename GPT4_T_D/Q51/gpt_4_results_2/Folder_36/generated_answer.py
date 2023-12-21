
from collections import defaultdict
import itertools

def if_contains_anagrams(words):
    anagrams = defaultdict(list)

    for word in words:
        simplified_word = ''.join(sorted(word.lower()))
        if len(simplified_word) >= 3:
            anagrams[simplified_word].append(word)

    pairs = 0
    for ana in anagrams.values():
        pairs += len(list(itertools.combinations(ana, 2)))

    return pairs <= 25
