
from collections import Counter

def if_contains_anagrams(lst):
    anagram_counter = 0
    sorted_words = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    word_counts = Counter(sorted_words)
    for count in word_counts.values():
        anagram_counter += count * (count - 1) // 2
    return anagram_counter >= 72
