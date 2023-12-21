
from collections import Counter

def if_contains_anagrams(lst):
    anagram_counter = 0
    sorted_list = ["".join(sorted(word.lower())) for word in lst if len(word) >= 3]
    counter = Counter(sorted_list)
    for count in counter.values():
        anagram_counter += count * (count-1) // 2
    return anagram_counter >= 61
