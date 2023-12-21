
from collections import Counter

def if_contains_anagrams(input_list):
    sorted_list = [''.join(sorted(word.lower())) for word in input_list if len(word) >= 3]
    counter = Counter(sorted_list)
    anagram_pairs = sum(val * (val-1) // 2 for val in counter.values())
    return anagram_pairs <= 24
