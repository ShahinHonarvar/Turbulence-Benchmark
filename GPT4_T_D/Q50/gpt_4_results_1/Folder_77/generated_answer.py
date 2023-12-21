
from collections import defaultdict

def if_contains_anagrams(strings):
    if not isinstance(strings, list):
        return False

    anagrams = defaultdict(list)

    for word in strings:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = "".join(sorted(word))
            anagrams[sorted_word].append(word)

    pairs = 0
    for anagram_list in anagrams.values():
        if len(anagram_list) > 1:
            pairs += len(anagram_list) * (len(anagram_list) - 1) // 2

    return pairs >= 209
