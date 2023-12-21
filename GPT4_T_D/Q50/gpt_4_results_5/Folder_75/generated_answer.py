
from collections import defaultdict

def if_contains_anagrams(words):
    word_map = defaultdict(list)
    for word in words:
        word_map[''.join(sorted(word.lower()))].append(word)

    anagram_pairs = 0
    for k, val in word_map.items():
        if len(k) >= 3:
            anagram_pairs += len(val) * (len(val) - 1) // 2
        if anagram_pairs >= 70:
            return True
    return False
