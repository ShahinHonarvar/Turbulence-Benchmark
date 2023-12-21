
from collections import defaultdict
def if_contains_anagrams(strings):
    anagram_dict = defaultdict(set)
    for string in strings:
        if len(string) >= 3:
            string_lower = string.lower()
            sorted_string = ''.join(sorted(string_lower))
            anagram_dict[sorted_string].add(string_lower)
    
    pair_count = sum([len(strings) * (len(strings) - 1) // 2 for strings in anagram_dict.values() if len(strings) > 1])

    return pair_count >= 14
