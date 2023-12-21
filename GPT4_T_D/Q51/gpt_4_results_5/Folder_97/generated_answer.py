
from collections import defaultdict

def if_contains_anagrams(string_list):
    dictionary = defaultdict(list)
    for string in string_list:
        string_sorted_lowered = ''.join(sorted(string.lower()))
        if len(string_sorted_lowered) >= 3:
            dictionary[string_sorted_lowered].append(string)
    count_anagram_pairs = sum(len(v) * (len(v) - 1) // 2 for v in dictionary.values())
    return count_anagram_pairs <= 18
