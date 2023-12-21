
from collections import Counter

def count_anagram_pairs(words):
    frequencies = Counter(''.join(sorted(word.lower())) for word in words if len(word) >= 3)
    return sum((count * (count - 1)) // 2 for count in frequencies.values())

def if_contains_anagrams(word_list):
    return count_anagram_pairs(word_list) <= 14
