
from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    sorted_strings = [''.join(sorted(s.lower())) for s in string_list if len(s) >= 3]
    for word, count in Counter(sorted_strings).items():
        anagram_count += count * (count - 1) // 2
    return anagram_count <= 18
