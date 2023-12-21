
from collections import Counter

def if_contains_anagrams(word_list):
    anagram_count = 0
    words = [''.join(sorted(word.lower())) for word in word_list if len(word) >= 3]
    counter = Counter(words)
    for word in counter:
        anagram_count += counter[word] * (counter[word] - 1) // 2
        if anagram_count > 19:
            return False
    return True
