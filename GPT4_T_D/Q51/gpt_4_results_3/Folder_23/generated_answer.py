
from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    string_list = [''.join(sorted(string.lower())) for string in string_list if len(string) >= 3]
    string_counter = Counter(string_list)

    for count in string_counter.values():
        anagram_count += count * (count - 1) // 2

    return anagram_count <= 49
