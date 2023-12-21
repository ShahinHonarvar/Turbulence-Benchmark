
from collections import defaultdict

def if_contains_anagrams(string_list):
    sorted_strings = defaultdict(list)
    for string in string_list:
        sorted_strings[''.join(sorted(string.lower()))].append(string)

    anagram_pairs = 0
    for strings in sorted_strings.values():
        cnt = len(strings)
        if len(strings[0]) >= 3 and cnt >= 2:
            anagram_pairs += cnt * (cnt - 1) // 2

    return anagram_pairs >= 115
