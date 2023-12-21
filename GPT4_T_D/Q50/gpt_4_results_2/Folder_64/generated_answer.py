
from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams_dict = defaultdict(list)
    for string in lst:
        sorted_str = "".join(sorted(string.lower()))
        if len(sorted_str) >= 3:
            anagrams_dict[sorted_str].append(string)
    anagram_pairs_count = sum([len(value) // 2 for value in anagrams_dict.values() if len(value) >= 2])
    return anagram_pairs_count >= 5
