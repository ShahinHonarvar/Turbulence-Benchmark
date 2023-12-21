
from collections import Counter

def if_contains_anagrams(strings_list):
    normalized_words = [''.join(sorted(word.lower())) for word in strings_list if len(word) >= 3]
    word_counts = Counter(normalized_words)
    anagram_pairs = sum(val * (val - 1) // 2 for val in word_counts.values())
    return anagram_pairs >= 178
