
from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    sorted_words = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    word_counts = Counter(sorted_words)
    for count in word_counts.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count >= 178
