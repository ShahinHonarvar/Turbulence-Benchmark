
from collections import Counter

def if_contains_anagrams(lst):
    sorted_strings = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    word_counts = Counter(sorted_strings)
    anagram_pairs = sum(count*(count-1)//2 for count in word_counts.values())
    return anagram_pairs >= 108
