
from collections import Counter


def if_contains_anagrams(words):
    anagram_pairs = 0

    words_sorted = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    count = Counter(words_sorted)

    for word, freq in count.items():
        if freq > 1:
            anagram_pairs += (freq * (freq - 1)) // 2

        if anagram_pairs >= 97:
            return True

    return False
