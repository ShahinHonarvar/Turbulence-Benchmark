
from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(set)
    for word in strings:
        if len(word) < 3: continue
        key = ''.join(sorted(word.lower()))
        anagrams[key].add(word)

    pairs = 0
    for word_set in anagrams.values():
        size = len(word_set)
        pairs += size * (size - 1) // 2
        if pairs > 94: return False

    return True
