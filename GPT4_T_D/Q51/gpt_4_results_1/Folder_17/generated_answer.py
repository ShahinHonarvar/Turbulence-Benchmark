
from collections import Counter

def if_contains_anagrams(word_list):
    formatted_words = [''.join(sorted(word.lower())) for word in word_list if len(word) >= 3]
    anagram_counter = Counter(formatted_words)

    anagram_pairs = sum(value * (value-1) // 2 for value in anagram_counter.values())

    return anagram_pairs <= 22
