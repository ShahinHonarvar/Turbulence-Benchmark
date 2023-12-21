
from collections import Counter

def if_contains_anagrams(word_list):
    sorted_words = [''.join(sorted(word.lower())) for word in word_list if len(word) >= 3]
    word_counts = Counter(sorted_words)
    anagram_counts = sum(count * (count - 1) // 2 for count in word_counts.values())
    return anagram_counts <= 40
