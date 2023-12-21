
from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    pair_count = 0

    for word in words:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)

    for sorted_words in anagram_dict.values():
        pairs = len(sorted_words)
        if pairs > 1:
            pair_count += pairs * (pairs - 1) // 2

    return pair_count >= 177
