
from collections import Counter
from itertools import combinations

def if_contains_anagrams(words_list):
    sorted_words = [''.join(sorted(word.lower())) for word in words_list if len(word) >= 3]
    freq_count = Counter(sorted_words)
    anagram_pairs = sum([(count * (count-1)) // 2 for count in freq_count.values()])
    return anagram_pairs >= 16
