
from collections import Counter

def if_contains_anagrams(words):
    anagram_counter = 0
    word_counter = Counter([''.join(sorted(word.lower())) for word in words if len(word) >= 3])
    for word, count in word_counter.items():
        anagram_counter += count * (count - 1) // 2
        if anagram_counter > 401:
            return False
    return True
