
from collections import Counter

def if_contains_anagrams(lst):
    anagram_pairs = 0
    anagrams = {}

    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word] = anagrams.get(sorted_word, []) + [word]

    for sorted_word, words in anagrams.items():
        count = len(words)
        if count > 1:
            anagram_pairs += count * (count - 1) // 2

    return True if anagram_pairs >= 96 else False
