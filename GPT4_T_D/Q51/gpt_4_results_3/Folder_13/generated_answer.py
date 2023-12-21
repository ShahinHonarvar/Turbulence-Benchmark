
from collections import Counter

def if_contains_anagrams(input_list):
    sorted_strings = [''.join(sorted(value.lower())) for value in input_list if len(value) >= 3]
    counter = Counter(sorted_strings)
    anagram_pairs = sum([(v*(v-1))//2 for k, v in counter.items() if v > 1])
    return anagram_pairs <= 54
