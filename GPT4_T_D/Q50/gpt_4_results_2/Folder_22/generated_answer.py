
from collections import Counter

def if_contains_anagrams(lst):
    sorted_word_list = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    word_freq = Counter(sorted_word_list)
    anagram_pairs = sum(freq*(freq-1)//2 for freq in word_freq.values())
    return anagram_pairs >= 72
